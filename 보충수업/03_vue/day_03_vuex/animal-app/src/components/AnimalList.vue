<template>
  <div>
    <h1>My Adorable Animal List</h1>
    <img
      v-for="image in getAnimalImages"
      :key="image"
      width="200"
      :src="image"
      alt="animal-image"
    >
  </div>
</template>

<script>
// 1. helpers 불러오기
import { mapGetters } from 'vuex'
export default {
  name: 'AnimalList',
  computed: {
    // 2. helpers 등록
    ...mapGetters(['getAnimalImages']),
    // animalImages() {
    //   return this.$store.getters.getAnimalImages
    // },
    // 3. helpers 사용
  },
}
</script>

<style>

</style>