#COMPONENTE COM GENERIC
interface Props<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}
export function List<T>({ items, renderItem }: Props<T>) {
  return <ul>{items.map((item, i) => <li key={i}>{renderItem(item)}</li>)}</ul>;
}
#USO
<List<string> items={['a', 'b']} renderItem={(i) => <span>{i}</span>} />