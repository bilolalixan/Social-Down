import Downloader from "./components/Downloader";
import Platforms from "./components/Platforms";
import HowItWorks from "./components/HowItWorks";

export default function Home() {
  return (
    <>
      {/* Header */}
      <header className="header">
        <div className="container header-inner">
          <div className="logo">Social Down</div>
          <nav className="nav">
            <a href="#platforms">Platformalar</a>
            <a href="#how">Qanday ishlaydi</a>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <main>
        <section className="hero container">
          <h1>
            Video va audiolarni<br />
            <span>tezda yuklab oling</span>
          </h1>
          <p>
            Instagram, TikTok, YouTube, Facebook va 50+ platformadan
            video va audio yuklab oling. Bepul va cheksiz.
          </p>

          {/* Stats */}
          <div className="stats">
            <div className="stat">
              <div className="stat-val">50+</div>
              <div className="stat-label">Platforma</div>
            </div>
            <div className="stat">
              <div className="stat-val">4K</div>
              <div className="stat-label">Maksimal sifat</div>
            </div>
            <div className="stat">
              <div className="stat-val">100%</div>
              <div className="stat-label">Bepul</div>
            </div>
          </div>

          <Downloader />
        </section>

        {/* Platforms */}
        <div id="platforms">
          <Platforms />
        </div>

        {/* How it works */}
        <div id="how">
          <HowItWorks />
        </div>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <p>© 2025 Social Down. Barcha huquqlar himoyalangan.</p>
        </div>
      </footer>
    </>
  );
}
