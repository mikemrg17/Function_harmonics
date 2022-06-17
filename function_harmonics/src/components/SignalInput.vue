<template>
  <div class="hello">
    <input id="signal" type="text" v-model="signal" placeholder="Ingrese la función de la señal">
    <br>
    <input type="number" v-model="less" class="period" placeholder="-T/2">
    &lt; t &le;
    <input type="number" v-model="greater" class="period" placeholder="T/2">
    <br>
    ¿Cuántos armónicos?  <input type="number" v-model="harmonics" id="harmonics">
    <br>
    <button id="operate" @click="operate">Computar</button>
  </div>
</template>

<script>
export default {
  name: 'SignalInput',
  data(){
    return{
      signal: "",
      less: "",
      greater: "",
      harmonics: 0
    }
  },
  methods:{
    operate(){
      let data = {
        signal: this.signal,
        less: this.less,
        greater: this.greater,
        harmonics: this.harmonics
      }

      this.$emit('operate-signal', data)
    }
  }
}
</script>

<style scoped>
  p{
    font-size: 1em;
  }

  #signal{
    color: #566573;
    font-size: 1em;
    width: 35%;
    padding: 12px 10px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  .period{
    color: #566573;
    font-size: 1em;
    width: 3%;
    padding: 12px 10px;
    margin: 8px 0;
    box-sizing: border-box;
  }

  .hello{
    margin-top: 3em;
  }

  #operate{
    width: 5%;
    font-size: 1em;
    color: white;
    height: 3em;
    border: none;
    background-color: #4285f4;
    border-radius: 0.3em;
    cursor: pointer;
  }

  input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
