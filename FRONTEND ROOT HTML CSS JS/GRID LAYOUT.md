# GRID CONTAINER
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 10px;
}

# GRID ITEM
.item {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}
