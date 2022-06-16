<script>
import VueP5 from 'vue-p5';

export default {
    name: 'SignalDisplayer',
    data(){
        return {
            slider : null,
            time: 0,
            wave: [],
            z: 100,
        }
    },
    methods: {
        setup(sketch) {
            sketch.createCanvas(800,400)
            sketch.background('white');
            this.slider = sketch.createSlider(1, 10 , 5)
        },
        draw(sketch){
            sketch.translate(150, 200);
            let x = 0;
            let y = 0;

            for (let i = 0; i < this.slider.value(); i++) {
                let prevx = x;
                let prevy = y;
                
                let n = i * 2 + 1;
                let radius = 75 * (4 / (n * Math.PI));
                x += radius * Math.cos(n * this.time);
                y += radius * Math.sin(n * this.time);

                sketch.stroke(0, 100);
                sketch.noFill();
                sketch.ellipse(prevx, prevy, radius * 2);

                sketch.stroke(0);
                sketch.line(prevx, prevy, x, y);
            }
            /*
            this.wave.unshift(y);
            sketch.translate(200, 0);
            sketch.line(x - 200, y, 0, this.wave[0]);
            sketch.beginShape();
            sketch.noFill();
            for (let i = 0; i < this.wave.length; i++) {
                sketch.vertex(i, this.wave[i]);
            }
            sketch.endShape();

            this.time += 0.05;

            if (this.wave.length > 250) {
                this.wave.pop();
            }*/
        }
    },

    render(h) {
        return h(VueP5, {on: this});
    }
};
</script>

<style>

</style>