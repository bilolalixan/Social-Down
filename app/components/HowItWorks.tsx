export default function HowItWorks() {
  const steps = [
    {
      step: "01",
      icon: (
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/>
          <path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/>
        </svg>
      ),
      title: "Havolani nusxalang",
      description: "Ijtimoiy tarmoqdan yuklamoqchi bo'lgan video yoki postning havolasini nusxalab oling.",
      color: "text-violet-400",
      bg: "bg-violet-500/15",
      border: "border-violet-500/20",
      glow: "shadow-violet-500/20",
    },
    {
      step: "02",
      icon: (
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="3"/>
          <path d="M3 9h18M9 21V9"/>
        </svg>
      ),
      title: "Havolani joylashtiring",
      description: "Nusxalangan havolani saytdagi maydonchaga joylashtiring va \"Yuklab olish\" tugmasini bosing.",
      color: "text-blue-400",
      bg: "bg-blue-500/15",
      border: "border-blue-500/20",
      glow: "shadow-blue-500/20",
    },
    {
      step: "03",
      icon: (
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M12 2v13M12 15l-4-4M12 15l4-4"/>
          <path d="M3 18h18"/>
        </svg>
      ),
      title: "Yuklab oling",
      description: "Kerakli sifat va formatni tanlang, so'ngra videoni qurilmangizga yuklab oling.",
      color: "text-emerald-400",
      bg: "bg-emerald-500/15",
      border: "border-emerald-500/20",
      glow: "shadow-emerald-500/20",
    },
  ];

  return (
    <section id="how-it-works" className="py-20 px-4 bg-gradient-to-b from-transparent to-[#0d0d15]">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-14">
          <span className="inline-block text-xs font-semibold uppercase tracking-widest text-violet-400 mb-3">
            Jarayon
          </span>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Qanday ishlaydi?
          </h2>
          <p className="text-slate-400 max-w-lg mx-auto">
            Atigi 3 ta oddiy qadam — video qurilmangizda
          </p>
        </div>

        {/* Steps */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {steps.map((item, i) => (
            <div key={item.step} className="relative">
              {/* Connector line */}
              {i < steps.length - 1 && (
                <div className="hidden md:block absolute top-10 left-[calc(100%-16px)] w-8 h-px bg-gradient-to-r from-white/10 to-white/5 z-10"/>
              )}

              <div className={`glass rounded-2xl p-6 border ${item.border} card-hover h-full`}>
                {/* Step number + icon */}
                <div className="flex items-center gap-3 mb-5">
                  <div className={`w-12 h-12 rounded-2xl ${item.bg} border ${item.border} flex items-center justify-center ${item.color} shadow-lg ${item.glow}`}>
                    {item.icon}
                  </div>
                  <span className="text-3xl font-black text-white/8 select-none">{item.step}</span>
                </div>

                <h3 className="text-lg font-bold text-white mb-2">{item.title}</h3>
                <p className="text-slate-400 text-sm leading-relaxed">{item.description}</p>
              </div>
            </div>
          ))}
        </div>

        {/* CTA */}
        <div className="text-center mt-12">
          <a
            href="#downloader"
            className="btn-gradient inline-flex items-center gap-2 text-white font-semibold px-8 py-3.5 rounded-2xl shadow-lg shadow-violet-500/25 text-sm"
          >
            <span>Hoziroq boshlang</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <path d="M12 2v13M12 15l-4-4M12 15l4-4" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M3 18h18" strokeLinecap="round"/>
            </svg>
          </a>
        </div>
      </div>
    </section>
  );
}
