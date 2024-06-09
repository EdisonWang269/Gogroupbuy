import liff from "@line/liff";
import store from "./store";

export const initializeLiff = async () => {
  try {
    await liff.init({ liffId: "2005547450-kezMVvEn" }).then(() => {
      if (!liff.isLoggedIn()) {
        console.log("not loggedIn");
        liff.login();
      } else {
        console.log("loggedIn");
        liff.getProfile().then(async (profile) => {
          console.log(profile.displayName);
          console.log(profile.userId);
          console.log(profile.pictureUrl);
          store.commit("user/setUserImg", profile.pictureUrl);
          store.commit("user/setUserID", profile.userId);
          store.commit("user/setUserName", profile.displayName);
          const response = await fetch(`/api/user`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              store_id: store.state.manager.storeID,
              userid: store.state.user.userID,
            }),
          });
          // You might want to handle the response here
          const responseData = await response.json();
          console.log(responseData);
        });
      }
    });
    console.log("LIFF initialized");
  } catch (error) {
    console.error("LIFF initialization failed", error);
  }
};

export default liff;
