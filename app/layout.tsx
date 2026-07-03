import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Social Down – Video Downloader",
  description:
    "Instagram, TikTok, YouTube, Facebook, Twitter va 50+ platformadan video va audio yuklab oling. Bepul, tez va qulay.",
  keywords: "video downloader, instagram, tiktok, youtube, facebook, twitter",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="uz">
      <body>{children}</body>
    </html>
  );
}
