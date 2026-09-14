// # SELECIONAR
const el = document.querySelector('.class');
const els = document.querySelectorAll('p');
const id = document.getElementById('id');

// # MODIFICAR
el.textContent = 'Texto';
el.innerHTML = '<span>Texto</span>';
el.style.color = 'red';
el.classList.add('nova-classe');
el.classList.remove('antiga-classe');
el.classList.toggle('ativa');
