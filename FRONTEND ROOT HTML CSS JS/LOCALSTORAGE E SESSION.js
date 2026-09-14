// # LOCALSTORAGE (PERSISTENTE)
localStorage.setItem('chave', 'valor');
const val = localStorage.getItem('chave');
localStorage.removeItem('chave');
localStorage.clear();

// # SESSIONSTORAGE (DURAÇÃO DA ABA)
sessionStorage.setItem('token', 'abc123XYZ');
const token = sessionStorage.getItem('token');
