export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: 'Arial, sans-serif', margin: 24 }}>
        <nav style={{ display: 'flex', gap: 12, marginBottom: 16 }}>
          <a href="/">Home</a><a href="/chat">Chat</a><a href="/procedure">Procedure</a><a href="/admin/approvals">Approvals</a><a href="/admin/audit">Audit</a>
        </nav>
        {children}
      </body>
    </html>
  );
}
