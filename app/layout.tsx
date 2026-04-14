import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Social Down – Video yuklovchi",
  description: "Instagram, TikTok, YouTube, Facebook, Twitter va 50+ platformadan video yuklab oling. Bepul, tez, qulay.",
  keywords: "video yuklovchi, instagram, tiktok, youtube, facebook, social down",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="uz">
      <body>{children}</body>
    </html>
  );
}
