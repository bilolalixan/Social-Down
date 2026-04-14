export default function Features() {
  const features = [
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
        </svg>
      ),
      title: "Ultra tez",
      description: "Yuqori tezlikdagi serverlar yordamida videolarni bir necha soniyada yuklab oling.",
      color: "text-yellow-400",
      bg: "bg-yellow-500/10",
      border: "border-yellow-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <rect x="3" y="11" width="18" height="11" rx="2"/>
          <path d="M7 11V7a5 5 0 0110 0v4"/>
        </svg>
      ),
      title: "100% Xavfsiz",
      description: "SSL shifrlash bilan himoyalangan. Hech qanday ma'lumotingiz saqlanmaydi.",
      color: "text-green-400",
      bg: "bg-green-500/10",
      border: "border-green-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <path d="M12 8v4l3 3"/>
        </svg>
      ),
      title: "Cheklovsiz",
      description: "Kuniga istalgancha video yuklab oling. Hech qanday limit yo'q, hisob kerak emas.",
      color: "text-blue-400",
      bg: "bg-blue-500/10",
      border: "border-blue-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>
        </svg>
      ),
      title: "4K Sifat",
      description: "360p dan 4K gacha barcha sifatlarda yuklab olish imkoniyati.",
      color: "text-purple-400",
      bg: "bg-purple-500/10",
      border: "border-purple-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/>
        </svg>
      ),
      title: "Ochiq manba",
      description: "GitHub'da mavjud. Hamjamiyat tomonidan qo'llab-quvvatlanadi va doimiy rivojlanadi.",
      color: "text-slate-400",
      bg: "bg-slate-500/10",
      border: "border-slate-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <rect x="5" y="2" width="14" height="20" rx="2"/>
          <path d="M12 18h.01"/>
        </svg>
      ),
      title: "Mobil qulay",
      description: "Telefon, planshet va kompyuterda bir xil qulay ishlaydi. Ilovani o'rnatish shart emas.",
      color: "text-cyan-400",
      bg: "bg-cyan-500/10",
      border: "border-cyan-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <path d="M9 18V5l12-2v13M9 18c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-2c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/>
        </svg>
      ),
      title: "Audio yuklovchi",
      description: "Video yoki faqat audio (MP3) formatida yuklab olish imkoniyati.",
      color: "text-pink-400",
      bg: "bg-pink-500/10",
      border: "border-pink-500/15",
    },
    {
      icon: (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <path d="M12 8c-2.2 0-4 1.8-4 4s1.8 4 4 4 4-1.8 4-4-1.8-4-4-4z"/>
        </svg>
      ),
      title: "Ro'yxatdan o'tish yo'q",
      description: "Hisob yaratish yoki tizimga kirish shart emas. To'g'ridan-to'g'ri yuklab oling.",
      color: "text-orange-400",
      bg: "bg-orange-500/10",
      border: "border-orange-500/15",
    },
  ];

  return (
    <section id="features" className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-14">
          <span className="inline-block text-xs font-semibold uppercase tracking-widest text-violet-400 mb-3">
            Nima uchun Social Down?
          </span>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Kuchli xususiyatlar
          </h2>
          <p className="text-slate-400 max-w-lg mx-auto">
            Boshqa yuklovchilardan farqli ravishda, Social Down tez, xavfsiz va bepul
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className={`glass rounded-2xl p-5 border ${feature.border} card-hover`}
            >
              <div className={`w-11 h-11 rounded-xl ${feature.bg} border ${feature.border} flex items-center justify-center ${feature.color} mb-4`}>
                {feature.icon}
              </div>
              <h3 className="text-white font-semibold text-sm mb-2">{feature.title}</h3>
              <p className="text-slate-500 text-xs leading-relaxed">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
