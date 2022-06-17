<template>
    <vue-p5 @sketch="sketch"></vue-p5>
</template>

<script>
import VueP5 from 'vue-p5';

export default {
    name: 'SignalDisplayer',
    components:{
        "vue-p5": VueP5
    },
    data(){
        return {
            slider : null,
            time: 0,
            wave: [],
            z: 100, 
        }
    },
    methods:{
        sketch(sk){
            sk.setup = () => {
                sk.createCanvas(800,400)
                this.slider = sk.createSlider(1, 10 , 5)
            },
            sk.draw = () => {
                sk.background('white')
                sk.translate(150, 200);
                var $vm = this

                let x = 0;
                let y = 0;

                for (let i = 0; i < $vm.slider.value(); i++) {
                    let prevx = x;
                    let prevy = y;

                    let n = i * 2 + 1;
                    let radius = 75 * (4 / (n * sk.PI));
                    x += radius * sk.cos(n * $vm.time);
                    y += radius * sk.sin(n * $vm.time);

                    sk.stroke(0, 100);
                    sk.noFill();
                    sk.ellipse(prevx, prevy, radius * 2);

                    sk.stroke(0);
                    sk.line(prevx, prevy, x, y);
                }
                $vm.wave.unshift(y);

                sk.translate(200, 0);
                sk.line(x - 200, y, 0, $vm.wave[0]);
                sk.beginShape();
                sk.noFill();
                for (let i = 0; i < $vm.wave.length; i++) {
                    sk.vertex(i, $vm.wave[i]);
                }
                sk.endShape();

                $vm.time += 0.05;

                if ($vm.wave.length > 250) {
                    $vm.wave.pop();
                }
            }
        }
    },
};
</script>

<style>

</style>