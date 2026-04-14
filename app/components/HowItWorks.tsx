const steps = [
  {
    n: 1,
    title: "Havolani nusxalang",
    desc: "Yuklamoqchi bo'lgan video yoki postning havolasini nusxalab oling.",
  },
  {
    n: 2,
    title: "Joylashtiring",
    desc: "Nusxalangan havolani yuqoridagi maydonga joylashtiring va tugmani bosing.",
  },
  {
    n: 3,
    title: "Yuklab oling",
    desc: "Kerakli sifatni tanlang va videoni qurilmangizga yuklab oling.",
  },
];

export default function HowItWorks() {
  return (
    <section id="how" style={{ padding: "80px 20px", background: "#0f0f13" }}>
      <div style={{ maxWidth: 900, margin: "0 auto" }}>
        <div style={{ textAlign: "center", marginBottom: 56 }}>
          <p className="section-label" style={{ marginBottom: 12 }}>Jarayon</p>
          <h2 style={{ fontSize: "clamp(26px,4vw,40px)", fontWeight: 800, color: "#f1f5f9" }}>
            Qanday ishlaydi?
          </h2>
          <p style={{ color: "#475569", fontSize: 16, marginTop: 12 }}>
            Atigi 3 ta qadam
          </p>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
          {steps.map((s, i) => (
            <div key={s.n} style={{ display: "flex", alignItems: "flex-start", gap: 20 }}>
              {/* Left: number + line */}
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", flexShrink: 0 }}>
                <div className="step-circle">{s.n}</div>
                {i < steps.length - 1 && (
                  <div style={{ width: 2, flex: 1, minHeight: 40, background: "linear-gradient(#7c3aed22, transparent)", marginTop: 8 }}/>
                )}
              </div>
              {/* Right: content */}
              <div className="platform-card" style={{ flex: 1, padding: "20px 22px", marginBottom: i < steps.length - 1 ? 0 : 0 }}>
                <h3 style={{ fontWeight: 700, fontSize: 17, color: "#e2e8f0", marginBottom: 6 }}>
                  {s.title}
                </h3>
                <p style={{ color: "#64748b", fontSize: 14, lineHeight: 1.6 }}>{s.desc}</p>
              </div>
            </div>
          ))}
        </div>

        <div style={{ textAlign: "center", marginTop: 48 }}>
          <a href="#downloader" style={{
            display: "inline-flex", alignItems: "center", gap: 8,
            padding: "14px 32px", borderRadius: 14,
            background: "linear-gradient(135deg,#7c3aed,#6366f1)",
            color: "#fff", fontWeight: 700, fontSize: 15, textDecoration: "none"
          }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="2.5">
              <path d="M12 3v12M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M4 19h16" strokeLinecap="round"/>
            </svg>
            Hoziroq boshlash
          </a>
        </div>
      </div>
    </section>
  );
}
