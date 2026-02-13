import { apiGet } from '../../../lib/api';

export default async function AuditPage() {
  const rows = await apiGet('/api/admin/audit-logs');
  return <main><h2>Audit Logs</h2><ul>{rows.map((r:any)=><li key={r.id}>{r.actor} - {r.action}</li>)}</ul></main>;
}
