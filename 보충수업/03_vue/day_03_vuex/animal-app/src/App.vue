<template>
  <div id="app">
    <button @click="FETCH_CAT_IMG">고양이 사진 보여주세요!</button>
    <AnimalList />
  </div>
</template>

<script>
// 1. helpers 불러오기
import { mapActions } from 'vuex'
// import { mapMutations } from 'vuex'
import AnimalList from '@/components/AnimalList.vue'
// import axios from 'axios'

export default {
  name: 'App',
  components: {
    AnimalList,
  },
  methods: {
    ...mapActions(['FETCH_CAT_IMG']),
    // 2. helpers 등록
    // UPDATE_ANIMAL_IMAGES() {}, 이렇게 만들어주는 것과 같다. => 3번같은 접근이 가능해진다.
    // ...mapMutations (['UPDATE_ANIMAL_IMAGES']),
    // async fetchCatImg() {
    //   const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
    //   const response = await axios.get(CAT_API_URL)
    //   const catImgUrl = response.data[0].url
    //   this.UPDATE_ANIMAL_IMAGES(catImgUrl)
      
        // .then((response) => {
        //   const catImgUrl = response.data[0].url
        //   // this.$store.commit('UPDATE_ANIMAL_IMAGES', catImgUrl)
        //   // 3. helpers사용(위 처럼 작성할 필요없다)
        //   this.UPDATE_ANIMAL_IMAGES(catImgUrl)
        // })
        // .catch((error) => {
        //   console.error(error)
        // })
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
