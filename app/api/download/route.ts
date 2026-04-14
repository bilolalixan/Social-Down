import { NextRequest, NextResponse } from "next/server";
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

function detectPlatform(url: string): string {
  if (/instagram\.com/i.test(url)) return "Instagram";
  if (/tiktok\.com/i.test(url)) return "TikTok";
  if (/youtube\.com|youtu\.be/i.test(url)) return "YouTube";
  if (/facebook\.com|fb\.com|fb\.watch/i.test(url)) return "Facebook";
  if (/twitter\.com|x\.com/i.test(url)) return "Twitter/X";
  if (/t\.me|telegram\.org/i.test(url)) return "Telegram";
  if (/vimeo\.com/i.test(url)) return "Vimeo";
  if (/pinterest\.com/i.test(url)) return "Pinterest";
  if (/twitch\.tv/i.test(url)) return "Twitch";
  if (/reddit\.com/i.test(url)) return "Reddit";
  return "Video";
}

function isValidUrl(url: string): boolean {
  try {
    const parsed = new URL(url);
    return ["http:", "https:"].includes(parsed.protocol);
  } catch {
    return false;
  }
}

function formatDuration(seconds: number): string {
  if (!seconds || isNaN(seconds)) return "";
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);
  if (h > 0) return `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  return `${m}:${String(s).padStart(2, "0")}`;
}

interface YtDlpFormat {
  format_id: string;
  ext: string;
  resolution?: string;
  height?: number;
  width?: number;
  filesize?: number;
  filesize_approx?: number;
  url: string;
  vcodec?: string;
  acodec?: string;
  abr?: number;
  quality?: number;
  format_note?: string;
}

interface YtDlpInfo {
  title: string;
  thumbnail: string;
  duration: number;
  formats: YtDlpFormat[];
  webpage_url: string;
}

export async function POST(request: NextRequest) {
  let url: string;

  try {
    const body = await request.json();
    url = body.url?.trim();
  } catch {
    return NextResponse.json({ error: "Noto'g'ri so'rov formati." }, { status: 400 });
  }

  if (!url) {
    return NextResponse.json({ error: "Havola kiritilmadi." }, { status: 400 });
  }

  if (!isValidUrl(url)) {
    return NextResponse.json({ error: "Havola noto'g'ri. To'liq URL manzilini kiriting." }, { status: 400 });
  }

  // Check if yt-dlp is available
  try {
    await execAsync("which yt-dlp || yt-dlp --version");
  } catch {
    // yt-dlp not installed — return demo data for development
    return NextResponse.json(getDemoResponse(url));
  }

  try {
    const { stdout } = await execAsync(
      `yt-dlp --dump-json --no-warnings --no-playlist "${url.replace(/"/g, "")}"`,
      { timeout: 30000 }
    );

    const info: YtDlpInfo = JSON.parse(stdout);

    // Filter and sort formats
    const formats = (info.formats || [])
      .filter((f: YtDlpFormat) => f.url && !f.url.startsWith("manifest"))
      .reduce((acc: YtDlpFormat[], f: YtDlpFormat) => {
        // Include video formats with audio, and audio-only
        const hasVideo = f.vcodec && f.vcodec !== "none";
        const hasAudio = f.acodec && f.acodec !== "none";
        if ((hasVideo && hasAudio) || (!hasVideo && hasAudio)) {
          acc.push(f);
        }
        return acc;
      }, [])
      .sort((a: YtDlpFormat, b: YtDlpFormat) => (b.height || 0) - (a.height || 0))
      .slice(0, 6)
      .map((f: YtDlpFormat) => {
        const hasVideo = f.vcodec && f.vcodec !== "none";
        const height = f.height || 0;

        let quality = "";
        if (hasVideo) {
          if (height >= 2160) quality = "4K (2160p)";
          else if (height >= 1440) quality = "1440p (2K)";
          else if (height >= 1080) quality = "1080p (Full HD)";
          else if (height >= 720) quality = "720p (HD)";
          else if (height >= 480) quality = "480p";
          else if (height >= 360) quality = "360p";
          else quality = f.format_note || `${height}p`;
        } else {
          quality = f.abr ? `Audio ${Math.round(f.abr)}kbps` : "Audio";
        }

        return {
          format_id: f.format_id,
          ext: f.ext,
          resolution: f.resolution || (height ? `${height}p` : "audio"),
          filesize: f.filesize || f.filesize_approx,
          url: f.url,
          quality,
        };
      });

    return NextResponse.json({
      title: info.title || "Video",
      thumbnail: info.thumbnail || "",
      duration: formatDuration(info.duration),
      platform: detectPlatform(url),
      formats,
    });
  } catch (err) {
    const error = err as Error;
    const msg = error.message || "";

    if (msg.includes("Private") || msg.includes("private")) {
      return NextResponse.json({ error: "Bu video yopiq (private). Faqat ochiq videolarni yuklab olish mumkin." }, { status: 400 });
    }
    if (msg.includes("Unsupported") || msg.includes("unsupported")) {
      return NextResponse.json({ error: "Bu platforma qo'llab-quvvatlanmaydi." }, { status: 400 });
    }
    if (msg.includes("404") || msg.includes("not found")) {
      return NextResponse.json({ error: "Video topilmadi. Havola noto'g'ri bo'lishi mumkin." }, { status: 404 });
    }

    return NextResponse.json(
      { error: "Videoni qayta ishlashda xato yuz berdi. Iltimos, qaytadan urinib ko'ring." },
      { status: 500 }
    );
  }
}

function getDemoResponse(url: string) {
  const platform = detectPlatform(url);
  return {
    title: `${platform} Video — Demo`,
    thumbnail: "",
    duration: "3:45",
    platform,
    formats: [
      { format_id: "1080", ext: "mp4", resolution: "1080p", filesize: 52428800, url: "#", quality: "1080p (Full HD)" },
      { format_id: "720", ext: "mp4", resolution: "720p", filesize: 26214400, url: "#", quality: "720p (HD)" },
      { format_id: "480", ext: "mp4", resolution: "480p", filesize: 10485760, url: "#", quality: "480p" },
      { format_id: "audio", ext: "mp3", resolution: "audio", filesize: 5242880, url: "#", quality: "Audio 128kbps" },
    ],
    _demo: true,
  };
}
