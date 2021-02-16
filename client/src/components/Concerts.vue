<template>
  <v-layout column>
    <v-flex xs6 offset-xs3>
      <b-card bg-variant="dark" text-variant="white" title="Concert">
           <b-icon class="nota1" icon="music-note" font-scale="3"></b-icon>
          <router-link :to="{name: 'concerts-create'}">
            <b-icon class="nota" icon="plus" font-scale="3.5"></b-icon>
          </router-link>

        <b-card columns>
          <div v-for="concert in concerts" :key="concert.id">
            <v-layout>
              <v-flex xs3>
                <div class="song-title">
                  {{concert.title}}
                </div>
                <div class="song-artist">
                  {{concert.artist}}
                </div>
                <div class="song-ganre">
                  {{concert.date}}
                </div>
                <br>
                <b-button
                  v-if = "$store.state.isUserLoggedIn"
                  class ="dugme"
                  @click = "deleteConcert(concert.id)">
                  Delete
                </b-button>

              </v-flex>

              <v-flex xs3>
                <img class="album-image" :src="concert.concertImageUrl" />
              </v-flex>
              <br> <br>  <br> <br>
            </v-layout>
          </div>
        </b-card>
      </b-card>
    </v-flex>
  </v-layout>
</template>

<script>
import Panel from './Panel'
import ConcertService from '../services/ConcertService'

export default {

  components: {
    Panel
  },
  data () {
    return {
      concerts: null
    }
  },
  methods: {
    navigateTo (route) {
      this.$router.push(route)
    },
    async deleteConcert (concertId) {
      this.error = null
      try {
        const nesto = await ConcertService.delete(concertId)
        console.log(nesto)
        for (let i = 0; i < this.concerts.length; i++) {
          if (this.concerts[i].id === concertId) {
            this.concerts.splice(i, 1)
          }
        }
      } catch (error) {
        console.log(error)
      }
    }
  },
  watch: {
    '$route.query.search': {
      immediate: true,
      async handler (value) {
        this.concerts = (await ConcertService.index(value)).data
      }
    }
  }
  // async mounted () {
  //   this.songs = (await SongsService.index()).data
  // }
}
</script>

<style scoped>
.album-image {
  margin-right: 70px;
}
.dugme {
  margin-right: 10px;
}
.song-ganre {
color: black;
font-size: 16px;
}
.song-title {
  color: black;
  font-size: 24px;
}
.song-artist {
  color: black;
  font-size: 20px;
}
.nota1 {
  margin-right: -1200px;
  margin-bottom: 15px;
}
.nota {
  margin-right: 1155px;
}
.album-image {
  width: 20%;
}
</style>
