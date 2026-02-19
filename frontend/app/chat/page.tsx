'use client';
import { useState } from 'react';
import { apiPost } from '../../lib/api';

export default function ChatPage() {
  const [q, setQ] = useState('');
  const [data, setData] = useState<any>(null);
  return <main><h2>Ask Policy</h2><input value={q} onChange={e => setQ(e.target.value)} placeholder='Ask a policy question' /> <button onClick={async()=>setData(await apiPost('/api/chat',{question:q,category:'general'}))}>Ask</button>
  {data && <div><p>{data.answer}</p><p>Score band: {data.retrieval_score_band} | Coverage: {data.citation_coverage}</p><ul>{data.citations?.map((c:any,i:number)=><li key={i}>{c.doc_id} - {c.section}</li>)}</ul></div>}</main>;
}
