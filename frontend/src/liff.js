import liff from '@line/liff';

export const initializeLiff = async () => {
  try {
    await liff.init({ liffId: '2004825262-RJxZEgg1' })
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
            })
        }
    }); // 替换成你的 LIFF ID
    console.log('LIFF initialized');
  } catch (error) {
    console.error('LIFF initialization failed', error);
  }
};

export default liff;