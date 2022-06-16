<template>
  <div class="hello">
    <input id="signal" type="text" v-model="signal" placeholder="Ingrese la función de la señal">
    <input type="text" v-model="period" id="period" placeholder="Ingrese el periodo">
    <button id="operate" @click="operate">Calcular</button>
  </div>
</template>

<script>
export default {
  name: 'SignalInput',
  data(){
    return{
      signal: "",
      period: ""
    }
  },
  methods:{
    operate(){
      let data = {
        signal: this.signal,
        period: this.period
      }

      this.$emit('operate-signal', data)
    }
  }
}
</script>

<style scoped>
  #signal{
    color: #566573;
    font-size: 1em;
    width: 35%;
    padding: 12px 10px;
    margin: 8px 0;
    box-sizing: border-box;
  }

  #period{
    color: #566573;
    font-size: 1em;
    width: 10%;
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
    background-color: #5499C7;
    border-radius: 0.3em;
    cursor: pointer;
  }
</style>
