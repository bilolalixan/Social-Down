import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Social Down – Ijtimoiy tarmoqlardan video yuklovchi",
  description: "Instagram, TikTok, YouTube, Facebook, Twitter va boshqa ijtimoiy tarmoqlardan video va rasmlarni bepul yuklab oling.",
  keywords: "video yuklovchi, instagram yuklovchi, tiktok yuklovchi, youtube yuklovchi, social down",
  openGraph: {
    title: "Social Down – Ijtimoiy tarmoqlardan video yuklovchi",
    description: "Instagram, TikTok, YouTube, Facebook, Twitter va boshqa ijtimoiy tarmoqlardan video va rasmlarni bepul yuklab oling.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="uz">
      <body className="min-h-screen">{children}</body>
    </html>
  );
}
