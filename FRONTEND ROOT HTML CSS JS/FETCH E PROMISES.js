// # PROMISES E FETCH
fetch('https://api.exemplo.com/dados')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// # ASYNC / AWAIT
async function getData() {
  try {
    const res = await fetch('https://api.exemplo.com/dados');
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
