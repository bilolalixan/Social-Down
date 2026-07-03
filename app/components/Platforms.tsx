const platforms = [
  { icon: "📸", name: "Instagram", color: "#e1306c" },
  { icon: "🎵", name: "TikTok", color: "#69c9d0" },
  { icon: "▶️", name: "YouTube", color: "#ff0000" },
  { icon: "👥", name: "Facebook", color: "#1877f2" },
  { icon: "🐦", name: "Twitter/X", color: "#1da1f2" },
  { icon: "✈️", name: "Telegram", color: "#229ed9" },
  { icon: "🎬", name: "Vimeo", color: "#1ab7ea" },
  { icon: "📌", name: "Pinterest", color: "#e60023" },
  { icon: "👾", name: "Reddit", color: "#ff4500" },
  { icon: "🎮", name: "Twitch", color: "#9147ff" },
  { icon: "🎧", name: "SoundCloud", color: "#ff5500" },
  { icon: "📹", name: "Dailymotion", color: "#0066dc" },
];

export default function Platforms() {
  return (
    <section className="section" style={{ background: "var(--bg2)", borderTop: "1px solid var(--border)", borderBottom: "1px solid var(--border)" }}>
      <div className="container">
        <div className="section-title">
          <h2>50+ Platforma qo&apos;llab-quvvatlanadi</h2>
          <p>Eng mashhur ijtimoiy tarmoqlar va video platformalardan yuklab oling</p>
        </div>
        <div className="platforms-grid">
          {platforms.map((p) => (
            <div key={p.name} className="platform-card">
              <span className="platform-icon">{p.icon}</span>
              <span className="platform-name">{p.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
