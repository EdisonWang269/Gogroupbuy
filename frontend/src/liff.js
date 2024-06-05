import liff from '@line/liff';
import store from './store';

export const initializeLiff = async () => {
  try {
    await liff.init({ liffId: '2004368945-ZXAjYNkb' })
    .then(() =>{
        if(!liff.isLoggedIn()){
            console.log("not loggedIn");
            liff.login();
        }
        else{
            console.log("loggedIn");
            liff.getProfile().then((profile) => {
              console.log(profile.displayName);
              console.log(profile.userId);
              console.log(profile.pictureUrl);
              store.commit("user/setUserImg",profile.pictureUrl);
              store.commit("user/setUserId",profile.userId);
              store.commit("user/setUserName",profile.displayName);
            })
        }
    }); 
    console.log('LIFF initialized');
  } catch (error) {
    console.error('LIFF initialization failed', error);
  }
};

export default liff;