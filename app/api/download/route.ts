import { NextRequest, NextResponse } from "next/server";

function isValidUrl(url: string) {
  try {
    const u = new URL(url);
    return u.protocol === "http:" || u.protocol === "https:";
  } catch {
    return false;
  }
}

// Cobalt API instances (public, free)
const COBALT_INSTANCES = [
  "https://cobalt.tools/api",
  "https://api.cobalt.tools",
];

export async function POST(req: NextRequest) {
  let url: string;
  try {
    const body = await req.json();
    url = body.url?.trim();
  } catch {
    return NextResponse.json({ error: "Noto'g'ri so'rov." }, { status: 400 });
  }

  if (!url) return NextResponse.json({ error: "Havola kiritilmadi." }, { status: 400 });
  if (!isValidUrl(url)) return NextResponse.json({ error: "Havola noto'g'ri. To'liq URL manzilini kiriting." }, { status: 400 });

  // Try each Cobalt instance
  for (const instance of COBALT_INSTANCES) {
    try {
      const response = await fetch(instance, {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url,
          videoQuality: "1080",
          audioFormat: "mp3",
          filenameStyle: "pretty",
        }),
        signal: AbortSignal.timeout(15000),
      });

      if (!response.ok) continue;

      const data = await response.json();

      // Cobalt returns status: redirect | stream | picker | error
      if (data.status === "error" || !data.status) continue;

      const results = [];

      if (data.status === "redirect" || data.status === "stream") {
        // Single video
        results.push({
          url: data.url,
          quality: "Video (En yaxshi sifat)",
          ext: "mp4",
          type: "video",
        });

        // Also try to get audio
        try {
          const audioRes = await fetch(instance, {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({ url, downloadMode: "audio", audioFormat: "mp3" }),
            signal: AbortSignal.timeout(10000),
          });
          if (audioRes.ok) {
            const audioData = await audioRes.json();
            if ((audioData.status === "redirect" || audioData.status === "stream") && audioData.url) {
              results.push({
                url: audioData.url,
                quality: "Faqat audio (MP3)",
                ext: "mp3",
                type: "audio",
              });
            }
          }
        } catch {
          // Audio optional, ignore errors
        }

        return NextResponse.json({
          results,
          title: extractTitle(url),
          thumbnail: "",
        });
      }

      if (data.status === "picker" && Array.isArray(data.picker)) {
        // Multiple items (e.g. Instagram carousel)
        for (const item of data.picker.slice(0, 6)) {
          if (item.url) {
            results.push({
              url: item.url,
              quality: item.type === "photo" ? "Rasm" : "Video",
              ext: item.type === "photo" ? "jpg" : "mp4",
              type: item.type === "photo" ? "video" : "video",
            });
          }
        }
        if (results.length > 0) {
          return NextResponse.json({ results, title: extractTitle(url), thumbnail: "" });
        }
      }
    } catch {
      continue;
    }
  }

  // Fallback error
  return NextResponse.json(
    {
      error:
        "Video yuklab bo'lmadi. Sabablari:\n• Havola noto'g'ri\n• Video yopiq (private)\n• Platforma qo'llab-quvvatlanmaydi\n\nYana bir marta urinib ko'ring.",
    },
    { status: 422 }
  );
}

function extractTitle(url: string): string {
  try {
    const u = new URL(url);
    const host = u.hostname.replace("www.", "").replace("m.", "");
    const map: Record<string, string> = {
      "instagram.com": "Instagram Video",
      "tiktok.com": "TikTok Video",
      "youtube.com": "YouTube Video",
      "youtu.be": "YouTube Video",
      "facebook.com": "Facebook Video",
      "twitter.com": "Twitter Video",
      "x.com": "Twitter/X Video",
      "vimeo.com": "Vimeo Video",
    };
    return map[host] || "Video";
  } catch {
    return "Video";
  }
}
