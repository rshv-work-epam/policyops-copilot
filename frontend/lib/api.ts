const base = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

export async function apiPost(path: string, body: unknown) {
  const res = await fetch(`${base}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-mock-user': 'demo.user', 'x-mock-role': 'admin' },
    body: JSON.stringify(body)
  });
  return res.json();
}

export async function apiGet(path: string) {
  const res = await fetch(`${base}${path}`, { headers: { 'x-mock-user': 'admin.user', 'x-mock-role': 'admin' }, cache: 'no-store' });
  return res.json();
}
