<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/titulo.png">
    <SignalInput @operate-signal="onOperate"/>
    <br>
    <p id="fourierS">Serie de fourier: {{fourier_serie}}</p>
    <hr>
    <div v-if="displayHarmonics == 1">
      <HarmonicsDisplay :fourier_serie="fourier_serie_split" />
    </div>
    <div v-if="serverActive == false">
      <h1 id="server-status">Servidor Inactivo</h1>
    </div>
  </div>
</template>

<script>
import SignalInput from './components/SignalInput.vue'
import HarmonicsDisplay from './components/HarmonicsDisplay.vue'
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      signal: "",
      less: 0,
      greater: 0,
      displayHarmonics: 0,
      serverActive: false,
      fourier_serie: "",
      fourier_serie_split: [],
      harmonics: 0
    }
  },
  components: {
    SignalInput,
    HarmonicsDisplay,
  },
  methods: {
    async compute(){
      axios.post('http://localhost:8000/compute', {
        signal: this.signal,
        less: this.less,
        greater: this.greater,
        harmonics: this.harmonics
      }).then((res) => {
        //Data reset
        this.fourier_serie_split = []
        this.fourier_serie = ""

        let fourierString = res.data
        let fourierStringReplaced = fourierString.replace(/\s/g, '')
        this.fourier_serie = fourierStringReplaced
        this.fourier_serie_split = fourierStringReplaced.split("+")
        this.displayHarmonics = 1
        
      }).catch((error) => {
        console.log(`POST request failed with ${error}`)
      })
    },
    onOperate(data){
      this.signal = data.signal
      this.less = data.less
      this.greater = data.greater
      this.harmonics = data.harmonics
      this.compute()
    }
  },
  async mounted(){
    axios.get('http://localhost:8000/').then((res)=>{
      console.log(res)
      this.serverActive = true
    }).catch((error)=>{
      console.log(error)
    })
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

hr{
  border:none;
  width: 90%;
  height: 50px;
  margin-top: 1em;
  border-bottom: 1px solid #D5D8DC;
  box-shadow: 0 20px 20px -20px #ABB2B9;
}

#server-status{
  font-size: 4em;
  color: red;
}

#fourierS{
  font-size: 1.5em;
  color: #ABB2B9;
}

#harmonics{
  color: #566573;
  height: 1%;
  font-size: 1em;
  width: 3%;
  padding: 12px 10px;
  margin: 8px 0;
  box-sizing: border-box;
}

</style>
