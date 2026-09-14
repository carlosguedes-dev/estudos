#DEFINIR E EXPORTAR INTERFACE
export interface User {
  id: string;
  name: string;
  email?: string;
}
#DEFINIR E EXPORTAR TYPE
export type Status = 'idle' | 'loading' | 'success' | 'error';
#IMPORTAR
import type { User, Status } from './types'