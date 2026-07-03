import { NextRequest, NextResponse } from "next/server";

const COBALT_INSTANCES = [
  "https://cobalt.tools/api",
  "https://api.cobalt.tools",
  "https://cob.itohq.net",
  "https://cobalt.catvibers.me",
];

interface CobaltResponse {
  status: "redirect" | "stream" | "picker" | "error" | "rate-limit" | "success";
  url?: string;
  urls?: string[];
  picker?: Array<{ type: string; url: string; thumb?: string; title?: string }>;
  error?: { code: string };
  text?: string;
}

function detectPlatform(url: string): string {
  if (/instagram\.com/i.test(url)) return "Instagram";
  if (/tiktok\.com/i.test(url)) return "TikTok";
  if (/youtube\.com|youtu\.be/i.test(url)) return "YouTube";
  if (/facebook\.com|fb\.watch/i.test(url)) return "Facebook";
  if (/twitter\.com|x\.com/i.test(url)) return "Twitter/X";
  if (/t\.me|telegram/i.test(url)) return "Telegram";
  if (/vimeo\.com/i.test(url)) return "Vimeo";
  if (/pinterest\.com/i.test(url)) return "Pinterest";
  if (/reddit\.com/i.test(url)) return "Reddit";
  if (/twitch\.tv/i.test(url)) return "Twitch";
  if (/soundcloud\.com/i.test(url)) return "SoundCloud";
  if (/dailymotion\.com/i.test(url)) return "Dailymotion";
  return "Noma'lum";
}

function getExtFromUrl(url: string, type: "video" | "audio"): string {
  const match = url.match(/\.(mp4|webm|mkv|mp3|m4a|ogg|opus)(\?|$)/i);
  if (match) return match[1].toLowerCase();
  return type === "audio" ? "mp3" : "mp4";
}

async function tryCobalt(
  instance: string,
  url: string
): Promise<CobaltResponse | null> {
  try {
    const res = await fetch(instance, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        url,
        videoQuality: "1080",
        audioFormat: "mp3",
        audioBitrate: "320",
        filenameStyle: "pretty",
      }),
      signal: AbortSignal.timeout(12000),
    });

    if (!res.ok) return null;
    const data = await res.json();
    return data as CobaltResponse;
  } catch {
    return null;
  }
}

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => ({}));
  const url: string = body?.url ?? "";

  if (!url || typeof url !== "string") {
    return NextResponse.json({ error: "URL talab qilinadi" }, { status: 400 });
  }

  let trimmed = url.trim();
  if (!trimmed.startsWith("http")) {
    trimmed = "https://" + trimmed;
  }

  const platform = detectPlatform(trimmed);

  // Try each Cobalt instance
  let cobaltData: CobaltResponse | null = null;
  for (const instance of COBALT_INSTANCES) {
    cobaltData = await tryCobalt(instance, trimmed);
    if (
      cobaltData &&
      cobaltData.status !== "error" &&
      cobaltData.status !== "rate-limit"
    ) {
      break;
    }
  }

  if (!cobaltData) {
    return NextResponse.json(
      { error: "Barcha serverlar vaqtinchalik mavjud emas. Keyinroq urinib ko'ring." },
      { status: 503 }
    );
  }

  const { status } = cobaltData;

  if (status === "error") {
    const code = cobaltData.error?.code ?? cobaltData.text ?? "unknown";
    const msg =
      code === "error.api.link.unsupported"
        ? "Bu platforma hali qo'llab-quvvatlanmaydi"
        : code === "error.api.fetch.short"
        ? "Qisqa havola qo'llab-quvvatlanmaydi, to'liq URL kiriting"
        : code === "error.api.content.post.unavailable"
        ? "Bu post yopiq yoki o'chirilgan"
        : `Xatolik: ${code}`;
    return NextResponse.json({ error: msg }, { status: 400 });
  }

  if (status === "rate-limit") {
    return NextResponse.json(
      { error: "Juda ko'p so'rov. Biroz kutib, qaytadan urinib ko'ring." },
      { status: 429 }
    );
  }

  type DlResult = { url: string; quality: string; ext: string; type: "video" | "audio" };
  const results: DlResult[] = [];

  if (status === "redirect" || status === "stream" || status === "success") {
    const dlUrl = cobaltData.url!;
    const isAudio =
      /\.(mp3|m4a|ogg|opus|flac|wav)(\?|$)/i.test(dlUrl) ||
      trimmed.includes("soundcloud");

    if (isAudio) {
      results.push({
        url: dlUrl,
        quality: "320kbps",
        ext: getExtFromUrl(dlUrl, "audio"),
        type: "audio",
      });
    } else {
      results.push({
        url: dlUrl,
        quality: "1080p",
        ext: getExtFromUrl(dlUrl, "video"),
        type: "video",
      });
    }
  } else if (status === "picker" && cobaltData.picker) {
    for (const item of cobaltData.picker.slice(0, 8)) {
      const isAudio = item.type === "audio";
      results.push({
        url: item.url,
        quality: isAudio ? "Audio" : "Video",
        ext: getExtFromUrl(item.url, isAudio ? "audio" : "video"),
        type: isAudio ? "audio" : "video",
      });
    }
  }

  if (results.length === 0) {
    return NextResponse.json(
      { error: "Yuklab olish havolasi topilmadi. URL to'g'ri ekanligini tekshiring." },
      { status: 400 }
    );
  }

  return NextResponse.json({
    results,
    platform,
    title: "",
    thumbnail: "",
  });
}
