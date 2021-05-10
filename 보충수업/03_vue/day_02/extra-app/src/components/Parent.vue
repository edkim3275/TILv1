<template>
  <div id="parent">
    <h1>Parent</h1>
    <input v-model="parentData" @input="onParentInput" type="text">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childInput }}</p>
    <Child
      :appData="appData"
      :parentData="parentData"
      @child-input="onChildInput"  
    />
  </div>
</template>

<script>
import Child from '@/components/Child'
export default {
  name: 'Parent',
  components: {
    Child,
  },
  data: function () {
    return {
      childInput: '',
      parentData: '',
    }
  },
  props: {  // 일종의 데이터 from 부모
    appData: String,
  },
  methods: {
    onChildInput(childInput) {
      this.childInput = childInput
      this.$emit('child-input', childInput)
    },
    onParentInput(parentInput) {
      const userInput = parentInput.target.value
      this.$emit('parent-input', userInput)
    }
  }
}
</script>

<style scoped>
  #parent {
    border: 1px solid red;
    margin: 48px;
  }
</style>