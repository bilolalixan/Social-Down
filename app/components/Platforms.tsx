export default function Platforms() {
  const platforms = [
    {
      name: "Instagram",
      description: "Reels, Stories, postlar va IGTV",
      color: "from-pink-500 to-purple-600",
      bg: "bg-gradient-to-br from-pink-500/10 to-purple-600/10",
      border: "border-pink-500/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <defs>
            <linearGradient id="ig2" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#f09433"/>
              <stop offset="50%" stopColor="#dc2743"/>
              <stop offset="100%" stopColor="#bc1888"/>
            </linearGradient>
          </defs>
          <rect x="2" y="2" width="20" height="20" rx="5" fill="url(#ig2)"/>
          <circle cx="12" cy="12" r="4.5" stroke="white" strokeWidth="1.8" fill="none"/>
          <circle cx="17.5" cy="6.5" r="1.2" fill="white"/>
        </svg>
      ),
    },
    {
      name: "TikTok",
      description: "Qisqa va uzun videolar",
      color: "from-slate-800 to-slate-900",
      bg: "bg-gradient-to-br from-slate-700/10 to-slate-900/10",
      border: "border-slate-500/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#010101"/>
          <path d="M16.5 8.3c-.8-.5-1.4-1.3-1.6-2.3h-2v9.5c0 1-.8 1.8-1.8 1.8s-1.8-.8-1.8-1.8.8-1.8 1.8-1.8c.2 0 .4 0 .6.1V11c-.2 0-.4-.1-.6-.1-2.1 0-3.8 1.7-3.8 3.8s1.7 3.8 3.8 3.8 3.8-1.7 3.8-3.8V10c.8.5 1.7.8 2.6.8V8.6c-.3.1-.6-.1-1-.3z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "YouTube",
      description: "HD, 4K videolar va Shorts",
      color: "from-red-500 to-red-700",
      bg: "bg-gradient-to-br from-red-500/10 to-red-700/10",
      border: "border-red-500/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#FF0000"/>
          <path d="M10 9l5 3-5 3V9z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "Facebook",
      description: "Video postlar va Reels",
      color: "from-blue-500 to-blue-700",
      bg: "bg-gradient-to-br from-blue-500/10 to-blue-700/10",
      border: "border-blue-500/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#1877F2"/>
          <path d="M13.5 8.5h1.5V6.5h-1.5c-1.7 0-3 1.3-3 3v1H9v2h1.5v5h2v-5H14l.5-2h-2V9.5c0-.6.4-1 1-1z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "Twitter / X",
      description: "Tvitlar va videolar",
      color: "from-slate-600 to-black",
      bg: "bg-gradient-to-br from-slate-600/10 to-black/10",
      border: "border-slate-500/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#000"/>
          <path d="M6.5 7h3l2.5 3.5L14.5 7H17l-4 5.5L17 17h-3l-2.5-3.5L9 17H6.5l4-5.5L6.5 7z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "Telegram",
      description: "Kanal va guruh videolari",
      color: "from-sky-400 to-blue-600",
      bg: "bg-gradient-to-br from-sky-400/10 to-blue-600/10",
      border: "border-sky-400/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#26A5E4"/>
          <path d="M17.5 7L6 11.5l3.5 1L11 17l2-2.5 3 2.5L17.5 7z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "Vimeo",
      description: "Professional sifatli videolar",
      color: "from-teal-400 to-cyan-600",
      bg: "bg-gradient-to-br from-teal-400/10 to-cyan-600/10",
      border: "border-teal-400/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#1ab7ea"/>
          <path d="M17.8 9c-.1 2.2-1.6 5.1-4.5 8.8C10.4 21.7 8 23 6 21.8c-1.8-1-2.6-4-2.4-7.5l.1-.8c.3-2.3 1-3.9 1.8-3.9.8 0 2 1.6 3.5 4.9.5-2.1 1.5-3.2 2.8-3.2.7 0 1.6.6 2.6 1.8.4-1.9 1-3 1.7-3 .8 0 1.5 1 1.7 2.9z" fill="white"/>
        </svg>
      ),
    },
    {
      name: "Pinterest",
      description: "Rasm va videolar",
      color: "from-red-400 to-red-600",
      bg: "bg-gradient-to-br from-red-400/10 to-red-600/10",
      border: "border-red-400/20",
      icon: (
        <svg width="32" height="32" viewBox="0 0 24 24">
          <rect x="2" y="2" width="20" height="20" rx="5" fill="#E60023"/>
          <path d="M12 4C7.6 4 4 7.6 4 12c0 3.4 2.1 6.3 5 7.6 0-.6 0-1.6.2-2.3l1.2-5s-.3-.6-.3-1.5c0-1.4.8-2.5 2-2.5.9 0 1.4.7 1.4 1.5 0 .9-.6 2.3-.9 3.6-.3 1.1.5 2 1.6 2 1.9 0 3.2-2.4 3.2-5.3 0-2.2-1.5-3.8-3.8-3.8-2.6 0-4.2 2-4.2 4 0 .8.3 1.6.7 2.1.1.1.1.2 0 .3l-.3 1c-.1.3-.3.4-.5.3C8.6 15.4 8 14 8 12.4c0-3 2.2-5.8 6.4-5.8 3.4 0 5.8 2.4 5.8 5.5 0 3.3-1.9 6-4.6 6-1 0-1.8-.5-2.1-1.1l-.6 2.2c-.2.8-.7 1.8-1.1 2.4.8.3 1.7.4 2.6.4 4.4 0 8-3.6 8-8S16.4 4 12 4z" fill="white"/>
        </svg>
      ),
    },
  ];

  return (
    <section id="platforms" className="py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-14">
          <span className="inline-block text-xs font-semibold uppercase tracking-widest text-violet-400 mb-3">
            Qo&apos;llab-quvvatlanadigan platformalar
          </span>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            50+ platformadan yuklab oling
          </h2>
          <p className="text-slate-400 max-w-xl mx-auto text-base">
            Barcha mashhur ijtimoiy tarmoqlar va video xizmatlaridan bir joyda yuklab oling
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          {platforms.map((platform) => (
            <div
              key={platform.name}
              className={`platform-icon glass rounded-2xl p-5 border ${platform.border} card-hover cursor-default`}
            >
              <div className="mb-3">{platform.icon}</div>
              <h3 className="text-white font-semibold text-sm mb-1">{platform.name}</h3>
              <p className="text-slate-500 text-xs leading-relaxed">{platform.description}</p>
            </div>
          ))}
        </div>

        {/* More */}
        <p className="text-center text-slate-500 text-sm mt-8">
          va yana 40+ platforma qo&apos;llab-quvvatlanadi...
        </p>
      </div>
    </section>
  );
}
