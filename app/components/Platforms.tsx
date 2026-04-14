const platforms = [
  { name: "Instagram", color: "#e1306c", desc: "Reels, Stories, Post" },
  { name: "TikTok",    color: "#010101", desc: "Video, Surovat" },
  { name: "YouTube",   color: "#ff0000", desc: "Video, Shorts, 4K" },
  { name: "Facebook",  color: "#1877f2", desc: "Video, Reels" },
  { name: "Twitter/X", color: "#000000", desc: "GIF, Video" },
  { name: "Telegram",  color: "#26a5e4", desc: "Kanal, Guruh" },
  { name: "Vimeo",     color: "#1ab7ea", desc: "HD Video" },
  { name: "Pinterest", color: "#e60023", desc: "Video, Rasm" },
];

export default function Platforms() {
  return (
    <section id="platforms" style={{ padding: "80px 20px", background: "#0c0c10" }}>
      <div style={{ maxWidth: 1100, margin: "0 auto" }}>
        <div style={{ textAlign: "center", marginBottom: 48 }}>
          <p className="section-label" style={{ marginBottom: 12 }}>Qo&apos;llab-quvvatlanadigan</p>
          <h2 style={{ fontSize: "clamp(26px,4vw,40px)", fontWeight: 800, color: "#f1f5f9" }}>
            50+ platformadan yuklab oling
          </h2>
        </div>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
          gap: 14
        }}>
          {platforms.map(p => (
            <div key={p.name} className="platform-card" style={{ padding: "20px 18px", display: "flex", alignItems: "center", gap: 14 }}>
              <div style={{
                width: 44, height: 44, borderRadius: 12,
                background: p.color, display: "flex", alignItems: "center",
                justifyContent: "center", flexShrink: 0,
                fontSize: 18, fontWeight: 800, color: "#fff"
              }}>
                {p.name[0]}
              </div>
              <div>
                <p style={{ fontWeight: 700, color: "#e2e8f0", fontSize: 15 }}>{p.name}</p>
                <p style={{ color: "#475569", fontSize: 12, marginTop: 2 }}>{p.desc}</p>
              </div>
            </div>
          ))}
        </div>

        <p style={{ textAlign: "center", color: "#334155", fontSize: 13, marginTop: 24 }}>
          va yana 40+ platforma...
        </p>
      </div>
    </section>
  );
}
