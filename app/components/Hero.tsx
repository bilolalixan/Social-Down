"use client";

import { useState, FormEvent, ReactElement } from "react";

interface VideoFormat {
  format_id: string;
  ext: string;
  resolution: string;
  filesize?: number;
  url: string;
  quality: string;
}

interface VideoInfo {
  title: string;
  thumbnail: string;
  duration: string;
  platform: string;
  formats: VideoFormat[];
  error?: string;
}

export default function Hero() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [videoInfo, setVideoInfo] = useState<VideoInfo | null>(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!url.trim()) return;

    setLoading(true);
    setError("");
    setVideoInfo(null);

    try {
      const res = await fetch("/api/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url.trim() }),
      });

      const data = await res.json();

      if (!res.ok || data.error) {
        setError(data.error || "Nimadir xato ketdi. Iltimos qaytadan urinib ko'ring.");
      } else {
        setVideoInfo(data);
      }
    } catch {
      setError("Server bilan ulanishda xato yuz berdi.");
    } finally {
      setLoading(false);
    }
  };

  const formatFileSize = (bytes?: number) => {
    if (!bytes) return "";
    const mb = bytes / (1024 * 1024);
    return mb >= 1 ? `${mb.toFixed(1)} MB` : `${(bytes / 1024).toFixed(0)} KB`;
  };

  const detectPlatform = (inputUrl: string) => {
    if (/instagram\.com/i.test(inputUrl)) return "Instagram";
    if (/tiktok\.com/i.test(inputUrl)) return "TikTok";
    if (/youtube\.com|youtu\.be/i.test(inputUrl)) return "YouTube";
    if (/facebook\.com|fb\.com/i.test(inputUrl)) return "Facebook";
    if (/twitter\.com|x\.com/i.test(inputUrl)) return "Twitter/X";
    if (/t\.me|telegram/i.test(inputUrl)) return "Telegram";
    return null;
  };

  const detected = detectPlatform(url);

  return (
    <section id="downloader" className="hero-bg min-h-screen flex flex-col items-center justify-center px-4 pt-24 pb-16">
      {/* Badge */}
      <div className="fade-in-up mb-6">
        <span className="inline-flex items-center gap-2 text-xs font-medium px-3.5 py-1.5 rounded-full border border-violet-500/30 text-violet-300 bg-violet-500/10">
          <span className="w-1.5 h-1.5 rounded-full bg-violet-400 pulse-glow inline-block"></span>
          Bepul &amp; Tez
        </span>
      </div>

      {/* Heading */}
      <h1 className="fade-in-up text-4xl sm:text-5xl md:text-6xl font-extrabold text-center leading-tight max-w-3xl mb-4" style={{animationDelay: "0.1s"}}>
        Ijtimoiy tarmoqlardan{" "}
        <span className="gradient-text">video yuklab oling</span>
      </h1>

      <p className="fade-in-up text-base sm:text-lg text-slate-400 text-center max-w-xl mb-10" style={{animationDelay: "0.2s"}}>
        Instagram, TikTok, YouTube, Facebook, Twitter va boshqa platformalardan videolarni bepul, tez va qulay yuklab oling.
      </p>

      {/* URL Input Form */}
      <div className="fade-in-up w-full max-w-2xl" style={{animationDelay: "0.3s"}}>
        <form onSubmit={handleSubmit} className="relative">
          <div className="flex items-center gap-3 glass rounded-2xl p-2 border border-white/8 focus-within:border-violet-500/50 transition-colors shadow-2xl">
            {/* Platform indicator */}
            <div className="flex-shrink-0 pl-2">
              {detected ? (
                <PlatformIcon name={detected} size={20} />
              ) : (
                <svg className="text-slate-500" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                  <path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/>
                  <path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/>
                </svg>
              )}
            </div>

            <input
              type="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Video havolasini bu yerga joylashtiring..."
              className="flex-1 bg-transparent text-white placeholder-slate-500 text-sm sm:text-base py-3 focus:outline-none"
              required
            />

            {url && (
              <button
                type="button"
                onClick={() => { setUrl(""); setVideoInfo(null); setError(""); }}
                className="text-slate-500 hover:text-slate-300 transition-colors flex-shrink-0 p-1"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M18 6L6 18M6 6l12 12"/>
                </svg>
              </button>
            )}

            <button
              type="submit"
              disabled={loading || !url.trim()}
              className="btn-gradient flex-shrink-0 flex items-center gap-2 text-white font-semibold px-5 sm:px-7 py-3 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            >
              {loading ? (
                <>
                  <svg className="spinner" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <circle cx="12" cy="12" r="10" strokeOpacity="0.3"/>
                    <path d="M12 2a10 10 0 0110 10"/>
                  </svg>
                  <span className="hidden sm:inline">Kutish...</span>
                </>
              ) : (
                <>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <path d="M12 2v13M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
                    <path d="M3 18h18" strokeLinecap="round"/>
                  </svg>
                  <span>Yuklab olish</span>
                </>
              )}
            </button>
          </div>
        </form>

        {/* Error */}
        {error && (
          <div className="mt-4 flex items-start gap-3 p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-300 text-sm fade-in-up">
            <svg className="flex-shrink-0 mt-0.5" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M12 8v4M12 16h.01"/>
            </svg>
            {error}
          </div>
        )}

        {/* Video Result */}
        {videoInfo && !error && (
          <div className="mt-6 glass rounded-2xl p-5 border border-white/8 fade-in-up">
            <div className="flex items-start gap-4 mb-5">
              {videoInfo.thumbnail && (
                <img
                  src={videoInfo.thumbnail}
                  alt={videoInfo.title}
                  className="w-24 h-16 sm:w-32 sm:h-20 object-cover rounded-xl flex-shrink-0 bg-white/5"
                />
              )}
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-white line-clamp-2 mb-1">{videoInfo.title}</p>
                <div className="flex flex-wrap items-center gap-2 mt-2">
                  {videoInfo.platform && (
                    <span className="text-xs px-2 py-0.5 rounded-full bg-violet-500/15 text-violet-300 border border-violet-500/20">
                      {videoInfo.platform}
                    </span>
                  )}
                  {videoInfo.duration && (
                    <span className="text-xs text-slate-400 flex items-center gap-1">
                      <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
                      </svg>
                      {videoInfo.duration}
                    </span>
                  )}
                </div>
              </div>
            </div>

            <div className="space-y-2">
              <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-3">Yuklab olish variantlari</p>
              {videoInfo.formats.map((fmt) => (
                <a
                  key={fmt.format_id}
                  href={fmt.url}
                  download
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-between p-3 rounded-xl bg-white/3 border border-white/6 hover:border-violet-500/40 hover:bg-violet-500/5 transition-all group"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-violet-500/15 flex items-center justify-center">
                      {fmt.ext === "mp3" || fmt.ext === "m4a" ? (
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" strokeWidth="2">
                          <path d="M9 18V5l12-2v13M9 18c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-2c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/>
                        </svg>
                      ) : (
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" strokeWidth="2">
                          <polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>
                        </svg>
                      )}
                    </div>
                    <div>
                      <p className="text-sm font-medium text-white">{fmt.quality}</p>
                      <p className="text-xs text-slate-500">{fmt.ext.toUpperCase()}{fmt.filesize ? ` · ${formatFileSize(fmt.filesize)}` : ""}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2 text-violet-400 group-hover:text-violet-300 transition-colors">
                    <span className="text-xs hidden sm:inline">Yuklab olish</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M12 2v13M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
                      <path d="M3 18h18" strokeLinecap="round"/>
                    </svg>
                  </div>
                </a>
              ))}
            </div>
          </div>
        )}

        {/* Hint */}
        {!videoInfo && !error && (
          <p className="text-center text-xs text-slate-600 mt-4">
            Qo&apos;llab-quvvatlanadigan: Instagram · TikTok · YouTube · Facebook · Twitter · Telegram · va ko&apos;proq
          </p>
        )}
      </div>

      {/* Stats */}
      <div className="fade-in-up flex flex-wrap justify-center gap-8 mt-16" style={{animationDelay: "0.4s"}}>
        {[
          { value: "10M+", label: "Yuklanmalar" },
          { value: "50+", label: "Platformalar" },
          { value: "100%", label: "Bepul" },
          { value: "4K", label: "Sifat" },
        ].map((stat) => (
          <div key={stat.label} className="text-center">
            <p className="text-2xl sm:text-3xl font-extrabold gradient-text">{stat.value}</p>
            <p className="text-xs text-slate-500 mt-0.5">{stat.label}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

function PlatformIcon({ name, size = 20 }: { name: string; size?: number }) {
  const icons: Record<string, ReactElement> = {
    Instagram: (
      <svg width={size} height={size} viewBox="0 0 24 24" fill="none">
        <defs>
          <linearGradient id="ig" x1="0%" y1="100%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#f09433"/>
            <stop offset="25%" stopColor="#e6683c"/>
            <stop offset="50%" stopColor="#dc2743"/>
            <stop offset="75%" stopColor="#cc2366"/>
            <stop offset="100%" stopColor="#bc1888"/>
          </linearGradient>
        </defs>
        <rect x="2" y="2" width="20" height="20" rx="5" fill="url(#ig)"/>
        <circle cx="12" cy="12" r="4.5" stroke="white" strokeWidth="1.8" fill="none"/>
        <circle cx="17.5" cy="6.5" r="1.2" fill="white"/>
      </svg>
    ),
    TikTok: (
      <svg width={size} height={size} viewBox="0 0 24 24" fill="none">
        <rect x="2" y="2" width="20" height="20" rx="5" fill="#010101"/>
        <path d="M16.5 8.3c-.8-.5-1.4-1.3-1.6-2.3h-2v9.5c0 1-.8 1.8-1.8 1.8s-1.8-.8-1.8-1.8.8-1.8 1.8-1.8c.2 0 .4 0 .6.1V11c-.2 0-.4-.1-.6-.1-2.1 0-3.8 1.7-3.8 3.8s1.7 3.8 3.8 3.8 3.8-1.7 3.8-3.8V10c.8.5 1.7.8 2.6.8V8.6c-.3.1-.6-.1-1-.3z" fill="white"/>
      </svg>
    ),
    YouTube: (
      <svg width={size} height={size} viewBox="0 0 24 24">
        <rect x="2" y="2" width="20" height="20" rx="5" fill="#FF0000"/>
        <path d="M10 9l5 3-5 3V9z" fill="white"/>
      </svg>
    ),
    Facebook: (
      <svg width={size} height={size} viewBox="0 0 24 24">
        <rect x="2" y="2" width="20" height="20" rx="5" fill="#1877F2"/>
        <path d="M13.5 8.5h1.5V6.5h-1.5c-1.7 0-3 1.3-3 3v1H9v2h1.5v5h2v-5H14l.5-2h-2V9.5c0-.6.4-1 1-1z" fill="white"/>
      </svg>
    ),
    "Twitter/X": (
      <svg width={size} height={size} viewBox="0 0 24 24">
        <rect x="2" y="2" width="20" height="20" rx="5" fill="#000"/>
        <path d="M6.5 7h3l2.5 3.5L14.5 7H17l-4 5.5L17 17h-3l-2.5-3.5L9 17H6.5l4-5.5L6.5 7z" fill="white"/>
      </svg>
    ),
    Telegram: (
      <svg width={size} height={size} viewBox="0 0 24 24">
        <rect x="2" y="2" width="20" height="20" rx="5" fill="#26A5E4"/>
        <path d="M17.5 7L6 11.5l3.5 1L11 17l2-2.5 3 2.5L17.5 7z" fill="white"/>
      </svg>
    ),
  };
  return icons[name] || null;
}
