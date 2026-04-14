"use client";

import { useState } from "react";
import Link from "next/link";

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 glass border-b border-white/5">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2.5 group">
            <div className="w-8 h-8 rounded-lg btn-gradient flex items-center justify-center shadow-lg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L12 16M12 16L7 11M12 16L17 11" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M3 18H21V20C21 21.1 20.1 22 19 22H5C3.9 22 3 21.1 3 20V18Z" fill="white" fillOpacity="0.8"/>
              </svg>
            </div>
            <span className="text-lg font-bold">
              <span className="gradient-text">Social</span>
              <span className="text-white"> Down</span>
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-6">
            <Link href="#platforms" className="text-sm text-slate-400 hover:text-white transition-colors">
              Platformalar
            </Link>
            <Link href="#how-it-works" className="text-sm text-slate-400 hover:text-white transition-colors">
              Qanday ishlaydi
            </Link>
            <Link href="#features" className="text-sm text-slate-400 hover:text-white transition-colors">
              Xususiyatlar
            </Link>
            <Link href="#faq" className="text-sm text-slate-400 hover:text-white transition-colors">
              FAQ
            </Link>
          </nav>

          {/* CTA */}
          <div className="hidden md:flex items-center gap-3">
            <a
              href="#downloader"
              className="btn-gradient text-white text-sm font-medium px-5 py-2.5 rounded-xl shadow-lg"
            >
              <span>Yuklab olish</span>
            </a>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden text-slate-400 hover:text-white transition-colors p-1"
            onClick={() => setMenuOpen(!menuOpen)}
            aria-label="Menu"
          >
            {menuOpen ? (
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M18 6L6 18M6 6l12 12"/>
              </svg>
            ) : (
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M3 12h18M3 6h18M3 18h18"/>
              </svg>
            )}
          </button>
        </div>

        {/* Mobile nav */}
        {menuOpen && (
          <div className="md:hidden py-4 border-t border-white/5">
            <nav className="flex flex-col gap-3">
              {["#platforms", "#how-it-works", "#features", "#faq"].map((href, i) => (
                <Link
                  key={href}
                  href={href}
                  className="text-sm text-slate-400 hover:text-white transition-colors py-1"
                  onClick={() => setMenuOpen(false)}
                >
                  {["Platformalar", "Qanday ishlaydi", "Xususiyatlar", "FAQ"][i]}
                </Link>
              ))}
              <a
                href="#downloader"
                className="btn-gradient text-white text-sm font-medium px-5 py-2.5 rounded-xl text-center mt-2"
                onClick={() => setMenuOpen(false)}
              >
                <span>Yuklab olish</span>
              </a>
            </nav>
          </div>
        )}
      </div>
    </header>
  );
}
