let shoppingCart = [
  {
    product: "자전거",
    qty: 1,
    price: 849.0,
  },
  {
    product: "에어팟",
    qty: 1,
    price: 249.0,
  },
  {
    product: "운동화",
    qty: 1,
    price: 90.99,
  },
  {
    product: "스웨터",
    qty: 2,
    price: 50.99,
  },
  {
    product: "양말",
    qty: 5,
    price: 5.99,
  },
];
const reducer = (acc, { qty, price }) => {
  return acc + qty * price;
};

const answer = shoppingCart.reduce(reducer, 0); // 0은 초기값, reducer 는 적용할 함수
