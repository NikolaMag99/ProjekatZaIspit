<template>
  <div>
    <b-card-group columns>
      <form>
        <div class="boks">
          <b-card bg-variant="dark" text-variant="white">
            <p class="h4 text-center mb-4">Concerts</p>
            <label for="defaultFormLoginEmailEx" class="grey-text">Title</label>
            <input type="email" id="defaultFormLoginEmailEx" class="form-control" v-model="concert.title"/>
            <br/>
            <label for="defaultFormLoginEmailEx" class="grey-text">Artist</label>
            <input type="email" class="form-control" v-model="concert.artist"/>
            <br/>
            <label for="defaultFormLoginEmailEx" class="grey-text">Capacity</label>
            <input type="email" class="form-control" v-model="concert.date"/>
            <br/>
            <label for="defaultFormLoginEmailEx" class="grey-text">Album Image Url</label>
            <input type="email" class="form-control" v-model="concert.concertImageUrl"/>
          </b-card>
        </div>
        <br>
        <b-button
          class="dugme"
          @click="create">
          Add New Concert
        </b-button>
      </form>
    </b-card-group>
  </div>
</template>

<script>
import Panel from './Panel'
import ConcertService from '../services/ConcertService'

export default {
  data () {
    return {
      concert: {
        title: null,
        artist: null,
        date: null,
        concertImageUrl: null
      }
    }
  },
  methods: {
    async create () {
      try {
        await ConcertService.post(this.concert)
        this.$router.push({
          name: 'concerts'
        })
      } catch (error) {
        console.log(error)
      }
    }
  },
  components: {
    Panel
  }
}
</script>

<style scoped>
.teksPolje {
  height: 250px;
}

.boks {
  margin-left: 200px;
}

.boks2 {
  margin-left: 300px;
  height: 630px;
  /*margin-right: 300px;*/
}

.dugme {
  margin-top: 700px;
  margin-left: -1100px;
}
</style>
