import { apiGet } from '../../../lib/api';

export default async function ApprovalsPage() {
  const rows = await apiGet('/api/admin/approvals');
  return <main><h2>Approvals Dashboard</h2><ul>{rows.map((r:any)=><li key={r.id}>#{r.id} {r.category} - {r.status}</li>)}</ul></main>;
}
