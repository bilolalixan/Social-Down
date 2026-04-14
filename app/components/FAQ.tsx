"use client";

import { useState } from "react";

const faqs = [
  {
    q: "Social Down bepulmi?",
    a: "Ha, Social Down to'liq bepul. Hech qanday to'lov yoki obuna talab qilinmaydi. Xizmatdan cheksiz foydalanishingiz mumkin.",
  },
  {
    q: "Ro'yxatdan o'tish kerakmi?",
    a: "Yo'q, hisob yaratish yoki tizimga kirish shart emas. Faqat havolani joylashtiring va yuklab oling.",
  },
  {
    q: "Qanday formatlar qo'llab-quvvatlanadi?",
    a: "MP4, WebM, MKV (video) va MP3, M4A (audio) formatlari qo'llab-quvvatlanadi. Sifatni 360p dan 4K gacha tanlash mumkin.",
  },
  {
    q: "Xususiy (private) postlarni yuklab olish mumkinmi?",
    a: "Yo'q, faqat ommaga ochiq (public) bo'lgan video va postlarni yuklab olish mumkin. Bu platformalar shartlariga mos keladi.",
  },
  {
    q: "Social Down qancha tez ishlaydi?",
    a: "Yuqori tezlikdagi serverlar yordamida yuklab olish jarayoni odatda 5-30 soniya ichida yakunlanadi.",
  },
  {
    q: "Qurilmalarimda ishlaydi?",
    a: "Ha, Social Down barcha qurilmalarda ishlaydi: mobil telefon (Android, iOS), planshet va kompyuter (Windows, Mac, Linux). Maxsus ilova o'rnatish shart emas.",
  },
];

export default function FAQ() {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <section id="faq" className="py-20 px-4 bg-gradient-to-b from-[#0d0d15] to-transparent">
      <div className="max-w-3xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <span className="inline-block text-xs font-semibold uppercase tracking-widest text-violet-400 mb-3">
            Savollar
          </span>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Ko&apos;p so&apos;raladigan savollar
          </h2>
        </div>

        {/* Accordion */}
        <div className="space-y-3">
          {faqs.map((faq, i) => (
            <div
              key={i}
              className={`glass rounded-2xl border transition-all duration-300 overflow-hidden ${
                open === i ? "border-violet-500/30" : "border-white/5 hover:border-white/10"
              }`}
            >
              <button
                className="w-full flex items-center justify-between p-5 text-left"
                onClick={() => setOpen(open === i ? null : i)}
              >
                <span className={`text-sm font-semibold transition-colors ${open === i ? "text-white" : "text-slate-300"}`}>
                  {faq.q}
                </span>
                <span className={`flex-shrink-0 ml-4 w-6 h-6 rounded-full flex items-center justify-center transition-all duration-300 ${
                  open === i ? "bg-violet-500 rotate-45" : "bg-white/5"
                }`}>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <path d="M12 5v14M5 12h14"/>
                  </svg>
                </span>
              </button>
              {open === i && (
                <div className="px-5 pb-5">
                  <p className="text-slate-400 text-sm leading-relaxed">{faq.a}</p>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
