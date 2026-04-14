"use client";

import { useState, FormEvent } from "react";

interface DownloadResult {
  url: string;
  quality: string;
  ext: string;
  type: "video" | "audio";
}

interface ApiResult {
  results: DownloadResult[];
  title?: string;
  thumbnail?: string;
  error?: string;
}

const PLATFORM_COLORS: Record<string, string> = {
  instagram: "#e1306c",
  tiktok: "#010101",
  youtube: "#ff0000",
  facebook: "#1877f2",
  twitter: "#000",
  x: "#000",
  telegram: "#26a5e4",
  vimeo: "#1ab7ea",
  pinterest: "#e60023",
};

function detectPlatform(url: string) {
  if (/instagram\.com/i.test(url)) return { name: "Instagram", key: "instagram" };
  if (/tiktok\.com/i.test(url)) return { name: "TikTok", key: "tiktok" };
  if (/youtube\.com|youtu\.be/i.test(url)) return { name: "YouTube", key: "youtube" };
  if (/facebook\.com|fb\.com|fb\.watch/i.test(url)) return { name: "Facebook", key: "facebook" };
  if (/twitter\.com|x\.com/i.test(url)) return { name: "Twitter/X", key: "twitter" };
  if (/t\.me|telegram/i.test(url)) return { name: "Telegram", key: "telegram" };
  if (/vimeo\.com/i.test(url)) return { name: "Vimeo", key: "vimeo" };
  if (/pinterest\.com/i.test(url)) return { name: "Pinterest", key: "pinterest" };
  return null;
}

export default function Downloader() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ApiResult | null>(null);
  const [error, setError] = useState("");

  const platform = url ? detectPlatform(url) : null;

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!url.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch("/api/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url.trim() }),
      });
      const data = await res.json();
      if (!res.ok || data.error) {
        setError(data.error || "Xato yuz berdi. Qaytadan urinib ko'ring.");
      } else {
        setResult(data);
      }
    } catch {
      setError("Server bilan ulanishda xato. Qaytadan urinib ko'ring.");
    } finally {
      setLoading(false);
    }
  };

  const clearAll = () => {
    setUrl("");
    setResult(null);
    setError("");
  };

  return (
    <div style={{ width: "100%", maxWidth: 660 }}>
      {/* Input */}
      <form onSubmit={handleSubmit}>
        <div className="url-box" style={{
          display: "flex", alignItems: "center", gap: 10,
          padding: "10px 10px 10px 16px"
        }}>
          {/* Platform indicator or link icon */}
          <div style={{ flexShrink: 0, display: "flex", alignItems: "center" }}>
            {platform ? (
              <div style={{
                width: 28, height: 28, borderRadius: 8,
                background: PLATFORM_COLORS[platform.key] || "#7c3aed",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontSize: 11, fontWeight: 700, color: "#fff"
              }}>
                {platform.name[0]}
              </div>
            ) : (
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#475569" strokeWidth="1.8">
                <path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/>
                <path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/>
              </svg>
            )}
          </div>

          <input
            type="url"
            value={url}
            onChange={e => { setUrl(e.target.value); setError(""); setResult(null); }}
            placeholder="Video havolasini bu yerga joylashtiring..."
            style={{
              flex: 1, background: "transparent", border: "none", outline: "none",
              color: "#e2e8f0", fontSize: 15, padding: "10px 0",
            }}
            autoFocus
          />

          {url && (
            <button type="button" onClick={clearAll} style={{
              background: "none", border: "none", cursor: "pointer",
              color: "#475569", padding: 6, display: "flex"
            }}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M18 6L6 18M6 6l12 12"/>
              </svg>
            </button>
          )}

          <button
            type="submit"
            disabled={loading || !url.trim()}
            className="btn-primary"
            style={{
              display: "flex", alignItems: "center", gap: 8,
              padding: "12px 24px", borderRadius: 12, fontSize: 15,
              whiteSpace: "nowrap", flexShrink: 0
            }}
          >
            {loading ? (
              <>
                <svg className="spin" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="2.5">
                  <path d="M12 2a10 10 0 0110 10" strokeLinecap="round"/>
                </svg>
                Yuklanmoqda...
              </>
            ) : (
              <>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="2.5">
                  <path d="M12 3v12M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M4 19h16" strokeLinecap="round"/>
                </svg>
                Yuklab olish
              </>
            )}
          </button>
        </div>
      </form>

      {/* Supported platforms hint */}
      {!result && !error && (
        <p style={{ textAlign: "center", color: "#334155", fontSize: 12, marginTop: 12 }}>
          Instagram · TikTok · YouTube · Facebook · Twitter · Telegram · va boshqalar
        </p>
      )}

      {/* Error */}
      {error && (
        <div style={{
          marginTop: 16, padding: "14px 18px", borderRadius: 12,
          background: "rgba(239,68,68,0.08)", border: "1px solid rgba(239,68,68,0.2)",
          color: "#fca5a5", fontSize: 14, display: "flex", alignItems: "flex-start", gap: 10
        }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{ flexShrink: 0, marginTop: 1 }}>
            <circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/>
          </svg>
          {error}
        </div>
      )}

      {/* Result */}
      {result && !error && (
        <div className="result-card" style={{ marginTop: 16, padding: 20 }}>
          {/* Video info */}
          <div style={{ display: "flex", gap: 14, marginBottom: 18, alignItems: "flex-start" }}>
            {result.thumbnail && (
              <img
                src={result.thumbnail}
                alt=""
                style={{ width: 100, height: 66, objectFit: "cover", borderRadius: 10, flexShrink: 0, background: "#2a2a38" }}
              />
            )}
            <div>
              {result.title && (
                <p style={{ color: "#e2e8f0", fontSize: 14, fontWeight: 600, lineHeight: 1.4,
                  display: "-webkit-box", WebkitLineClamp: 2, WebkitBoxOrient: "vertical", overflow: "hidden" }}>
                  {result.title}
                </p>
              )}
              {platform && (
                <span style={{
                  marginTop: 8, display: "inline-block", padding: "3px 10px", borderRadius: 999,
                  background: "rgba(124,58,237,0.15)", color: "#a78bfa", fontSize: 12, fontWeight: 600
                }}>
                  {platform.name}
                </span>
              )}
            </div>
          </div>

          {/* Download buttons */}
          <p style={{ color: "#475569", fontSize: 11, fontWeight: 700, letterSpacing: "0.08em",
            textTransform: "uppercase", marginBottom: 10 }}>
            Yuklab olish
          </p>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {result.results.map((item, i) => (
              <a
                key={i}
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                className="format-row"
              >
                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                  <div style={{
                    width: 36, height: 36, borderRadius: 10,
                    background: "rgba(124,58,237,0.15)",
                    display: "flex", alignItems: "center", justifyContent: "center"
                  }}>
                    {item.type === "audio" ? (
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" strokeWidth="2">
                        <path d="M9 18V5l12-2v13M9 18c0 1.1-1.34 2-3 2s-3-.9-3-2 1.34-2 3-2 3 .9 3 2zm12-2c0 1.1-1.34 2-3 2s-3-.9-3-2 1.34-2 3-2 3 .9 3 2z"/>
                      </svg>
                    ) : (
                      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" strokeWidth="2">
                        <polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>
                      </svg>
                    )}
                  </div>
                  <div>
                    <p style={{ color: "#e2e8f0", fontWeight: 600, fontSize: 14 }}>{item.quality}</p>
                    <p style={{ color: "#475569", fontSize: 12 }}>{item.ext.toUpperCase()}</p>
                  </div>
                </div>
                <div style={{ display: "flex", alignItems: "center", gap: 6, color: "#7c3aed" }}>
                  <span style={{ fontSize: 13, fontWeight: 600 }}>Yuklab olish</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <path d="M12 3v12M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
                    <path d="M4 19h16" strokeLinecap="round"/>
                  </svg>
                </div>
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
