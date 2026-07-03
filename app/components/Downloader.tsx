"use client";

import { useState } from "react";

interface DownloadResult {
  url: string;
  quality: string;
  ext: string;
  type: "video" | "audio";
}

interface ApiResponse {
  results: DownloadResult[];
  title?: string;
  thumbnail?: string;
  platform?: string;
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
  return "";
}

function getPlatformHint(url: string): { label: string; color: string } | null {
  const p = detectPlatform(url);
  if (!p) return null;
  const colors: Record<string, string> = {
    Instagram: "#e1306c",
    TikTok: "#69c9d0",
    YouTube: "#ff0000",
    "Facebook": "#1877f2",
    "Twitter/X": "#1da1f2",
    Telegram: "#229ed9",
    Vimeo: "#1ab7ea",
    Pinterest: "#e60023",
    Reddit: "#ff4500",
    Twitch: "#9147ff",
    SoundCloud: "#ff5500",
    Dailymotion: "#0066dc",
  };
  return { label: p, color: colors[p] || "#6c63ff" };
}

export default function Downloader() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<ApiResponse | null>(null);

  const hint = getPlatformHint(url);

  async function handleDownload() {
    const trimmed = url.trim();
    if (!trimmed) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch("/api/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: trimmed }),
      });

      const data = await res.json();

      if (!res.ok || data.error) {
        setError(data.error || "Xatolik yuz berdi. URL to'g'ri ekanligini tekshiring.");
        return;
      }

      setResult(data);
    } catch {
      setError("Server bilan bog'lanishda xatolik. Qaytadan urinib ko'ring.");
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "Enter") handleDownload();
  }

  return (
    <div className="dl-box">
      <div className="input-row">
        <input
          className="url-input"
          type="url"
          placeholder="Video havolasini shu yerga joylashtiring..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          onKeyDown={handleKeyDown}
          autoFocus
        />
        <button
          className="btn-primary"
          onClick={handleDownload}
          disabled={loading || !url.trim()}
        >
          {loading ? (
            <span style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <span className="spinner" />
              Yuklanmoqda...
            </span>
          ) : (
            "Yuklash"
          )}
        </button>
      </div>

      {hint && (
        <div className="platform-hint">
          <span
            className="hint-dot"
            style={{ background: hint.color }}
          />
          <span>
            {hint.label} havolasi aniqlandi
          </span>
        </div>
      )}

      {error && <div className="error-msg">{error}</div>}

      {result && (
        <div className="result-box">
          <div className="result-header">
            {result.thumbnail && (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                src={result.thumbnail}
                alt="Thumbnail"
                className="result-thumb"
              />
            )}
            <div>
              <div className="result-title">
                {result.title || "Video"}
              </div>
              {result.platform && (
                <div className="result-platform">{result.platform}</div>
              )}
            </div>
          </div>

          <div className="result-links">
            {result.results.map((item, i) => (
              <div className="dl-row" key={i}>
                <div className="dl-info">
                  <span className={`dl-type ${item.type}`}>
                    {item.type === "video" ? "Video" : "Audio"}
                  </span>
                  <span className="dl-quality">{item.quality}</span>
                  <span className="dl-ext">.{item.ext}</span>
                </div>
                <a
                  href={item.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn-dl"
                  download
                >
                  Yuklab olish
                </a>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
