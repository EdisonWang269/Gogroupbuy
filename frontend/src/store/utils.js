export function changeDate(oldDate) {
  const date = new Date(oldDate);
  const year = date.getFullYear();
  const month = ("0" + (date.getMonth() + 1)).slice(-2);
  const day = ("0" + date.getDate()).slice(-2);

  return `${year}/${month}/${day}`;
}

export function changeStatus(status) {
  if (typeof status === "number" || Number.isInteger(status)) {
    switch (status) {
      case -1:
        return "未到貨";
      case 0:
        return "待領取";
      case 1:
        return "已領取";
      default:
        return "未到貨";
    }
  } else {
    return status;
  }
}

export function formatOrder(order) {
  if (order.due_date !== "未到貨") {
    order.due_date = changeDate(order.due_date);
  }
  order.receive_status = changeStatus(order.receive_status);
  return order;
}

