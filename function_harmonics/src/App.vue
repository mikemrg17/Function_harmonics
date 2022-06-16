<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/titulo.png">
    <SignalInput @operate-signal="onOperate"/>
    <HarmonicsDisplay />
    <SignalDisplayer />
  </div>
</template>

<script>
import SignalInput from './components/SignalInput.vue'
import HarmonicsDisplay from './components/HarmonicsDisplay.vue'
import SignalDisplayer from './components/SignalDisplayer.vue'

export default {
  name: 'App',
  data(){
    return {
      signal: "",
      period: ""
    }
  },
  components: {
    SignalInput,
    HarmonicsDisplay,
    SignalDisplayer
  },
  methods: {
    onOperate(data){
      this.signal = data.signal
      this.period = data.period
    }
  }
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
