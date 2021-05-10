<template>
  <div id="child">
    <h1>Child</h1>
    <input @input="onInput" type="text">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: String,
    parentData: String,
  },
  methods: {
    onInput(event) {
      const userInput = event.target.value
      // 부모 컴포넌트와 자식 컴포넌트간의 약속된 이름
      this.$emit('child-input', userInput)
    },
  },
}
</script>

<style>
  #child {
    border: 1px solid blue;
    margin: 48px;
  }
</style>