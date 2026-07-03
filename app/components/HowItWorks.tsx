const steps = [
  {
    num: "1",
    title: "Havolani nusxalang",
    desc: "Video yoki audio yuklamoqchi bo'lgan platformadan havolani nusxalab oling.",
  },
  {
    num: "2",
    title: "Joylashtiring",
    desc: "Nusxalangan havolani yuqoridagi maydoniga joylashtiring va \"Yuklash\" tugmasini bosing.",
  },
  {
    num: "3",
    title: "Yuklab oling",
    desc: "Kerakli format va sifatni tanlang, keyin yuklab olish tugmasini bosing.",
  },
];

export default function HowItWorks() {
  return (
    <section className="section">
      <div className="container">
        <div className="section-title">
          <h2>Qanday ishlaydi?</h2>
          <p>3 ta oddiy qadamda videoni yuklab oling</p>
        </div>
        <div className="steps-grid">
          {steps.map((s) => (
            <div key={s.num} className="step-card">
              <div className="step-num">{s.num}</div>
              <h3>{s.title}</h3>
              <p>{s.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
