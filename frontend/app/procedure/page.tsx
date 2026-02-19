'use client';
import { useState } from 'react';
import { apiPost } from '../../lib/api';

export default function ProcedurePage() {
  const [state, setState] = useState<any>(null);
  return <main><h2>Guided Procedure</h2><button onClick={async()=>setState(await apiPost('/api/procedure/start',{procedure_name:'Employee Expense Reimbursement'}))}>Start Expense Procedure</button>
  {state && <pre>{JSON.stringify(state,null,2)}</pre>}</main>;
}
