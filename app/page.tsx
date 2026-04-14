import Downloader from "./components/Downloader";
import Platforms from "./components/Platforms";
import HowItWorks from "./components/HowItWorks";

export default function Home() {
  return (
    <div style={{ minHeight: "100vh", background: "#0f0f13" }}>
      {/* ── Header ── */}
      <header style={{
        position: "fixed", top: 0, left: 0, right: 0, zIndex: 50,
        background: "rgba(15,15,19,0.85)", backdropFilter: "blur(12px)",
        borderBottom: "1px solid #1e1e2e", height: 60,
        display: "flex", alignItems: "center"
      }}>
        <div style={{ maxWidth: 1100, margin: "0 auto", width: "100%", padding: "0 20px",
          display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          {/* Logo */}
          <a href="/" style={{ display: "flex", alignItems: "center", gap: 10, textDecoration: "none" }}>
            <div style={{
              width: 34, height: 34, borderRadius: 10,
              background: "linear-gradient(135deg,#7c3aed,#6366f1)",
              display: "flex", alignItems: "center", justifyContent: "center"
            }}>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                <path d="M12 3v12M12 15l-4-4M12 15l4-4" stroke="#fff" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M4 19h16" stroke="#fff" strokeWidth="2.5" strokeLinecap="round"/>
              </svg>
            </div>
            <span style={{ fontWeight: 700, fontSize: 18, color: "#fff" }}>
              Social<span style={{ color: "#a78bfa" }}>Down</span>
            </span>
          </a>

          {/* Nav */}
          <nav style={{ display: "flex", alignItems: "center", gap: 28 }}>
            {[
              ["Platformalar", "#platforms"],
              ["Qanday ishlaydi", "#how"],
            ].map(([label, href]) => (
              <a key={href} href={href} className="nav-link">
                {label}
              </a>
            ))}
            <a href="#downloader" style={{
              background: "linear-gradient(135deg,#7c3aed,#6366f1)",
              color: "#fff", fontSize: 13, fontWeight: 600,
              padding: "8px 18px", borderRadius: 10, textDecoration: "none"
            }}>
              Yuklab olish
            </a>
          </nav>
        </div>
      </header>

      <main>
        {/* ── Hero + Downloader ── */}
        <section id="downloader" style={{
          minHeight: "100vh", display: "flex", flexDirection: "column",
          alignItems: "center", justifyContent: "center",
          padding: "100px 20px 60px",
          background: `
            radial-gradient(ellipse 70% 60% at 20% 40%, rgba(124,58,237,0.12) 0%, transparent 60%),
            radial-gradient(ellipse 50% 50% at 80% 60%, rgba(99,102,241,0.08) 0%, transparent 60%),
            #0f0f13
          `
        }}>
          {/* Badge */}
          <div style={{
            display: "inline-flex", alignItems: "center", gap: 8, marginBottom: 24,
            padding: "6px 16px", borderRadius: 999,
            border: "1px solid rgba(124,58,237,0.35)",
            background: "rgba(124,58,237,0.08)", color: "#c4b5fd", fontSize: 13
          }}>
            <span style={{ width: 7, height: 7, borderRadius: "50%", background: "#a78bfa", display: "inline-block" }}/>
            Bepul · Tez · Reklama yo&apos;q
          </div>

          {/* Heading */}
          <h1 style={{
            fontSize: "clamp(32px, 5vw, 58px)", fontWeight: 800,
            textAlign: "center", lineHeight: 1.15, marginBottom: 16,
            color: "#f1f5f9", maxWidth: 720
          }}>
            Ijtimoiy tarmoqlardan{" "}
            <span className="gradient-text">video yuklab oling</span>
          </h1>

          <p style={{
            color: "#64748b", textAlign: "center", fontSize: "clamp(15px, 2vw, 18px)",
            maxWidth: 520, marginBottom: 48, lineHeight: 1.7
          }}>
            Instagram, TikTok, YouTube, Facebook, Twitter va 50+ platformadan
            videolarni bepul yuklab oling.
          </p>

          <Downloader />

          {/* Stats */}
          <div style={{
            display: "flex", gap: 48, marginTop: 56, flexWrap: "wrap", justifyContent: "center"
          }}>
            {[
              ["50+", "Platforma"],
              ["1080p", "Sifat"],
              ["100%", "Bepul"],
              ["0", "Ro'yxatdan o'tish"],
            ].map(([val, label]) => (
              <div key={label} style={{ textAlign: "center" }}>
                <div className="gradient-text" style={{ fontSize: 28, fontWeight: 800 }}>{val}</div>
                <div style={{ color: "#475569", fontSize: 13, marginTop: 2 }}>{label}</div>
              </div>
            ))}
          </div>
        </section>

        <Platforms />
        <HowItWorks />
      </main>

      {/* ── Footer ── */}
      <footer style={{
        borderTop: "1px solid #1e1e2e", padding: "32px 20px",
        textAlign: "center", color: "#334155", fontSize: 13
      }}>
        <p>© {new Date().getFullYear()} SocialDown · Faqat shaxsiy foydalanish uchun</p>
      </footer>
    </div>
  );
}
