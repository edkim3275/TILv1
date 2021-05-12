import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  // state는 데이터
  state: {  // data
    // 사용할 것을 만들어 놓는다(url하나하나 담을 리스트)
    animalImages: [],
  },
  getters: {  // computed
    // state가 인자로 자동으로 들어온다
    getAnimalImages(state) {
      return state.animalImages
    },
  },
  mutations: {  // methods
    // state를 변경하는 함수
    // state를 인자로 받고, 두번쨰로 받으려고하는 인자(다른 컴포넌트에서 받아옴)를 정해준다(이름 임의로 정하기)
    UPDATE_ANIMAL_IMAGES(state, imgUrl) {
      state.animalImages.push(imgUrl)
    },
  },
  actions: {
    async FETCH_CAT_IMG( { commit }) {
      // context: commit, dispatch, state..들이 들어옵니다.
      // 인자로 {}넣어서 필요한 인자들만 넣어 줄수가있습니다.
      const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
      try {
        const response = await axios.get(CAT_API_URL)
        const catImgUrl = response.data[0].url
        commit('UPDATE_ANIMAL_IMAGES', catImgUrl)
      } catch(err) {
        console.error(err)
      }
    },
  },
  modules: {
  }
})