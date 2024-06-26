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
  
  if(order.user_name === null){
    order.receive_status = "已領取";
  }
  else{
    order.receive_status = changeStatus(order.receive_status);
  }
  return order;
}

export function formatItem(item) {
  item.statement_date = changeDate(item.statement_date);
  return item;
}

export function base64ToBlob(base64, mime) {
  const byteCharacters = atob(base64);
  const byteNumbers = new Array(byteCharacters.length);
  for (let i = 0; i < byteCharacters.length; i++) {
    byteNumbers[i] = byteCharacters.charCodeAt(i);
  }
  const byteArray = new Uint8Array(byteNumbers);
  return new Blob([byteArray], { type: mime });
}

export function getImgURL(blob){
  if(blob){
    return URL.createObjectURL(blob);
  }
  return null;
}

