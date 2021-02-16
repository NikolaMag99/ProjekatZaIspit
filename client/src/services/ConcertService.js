import Api from '@/services/Api'

export default{
  index (search) {
    return Api().get('concerts', {
      params: {
        search: search
      }
    })
  },
  show (concertId) {
    return Api().get(`concerts/${concertId}`)
  },
  post (concert) {
    return Api().post('concerts', concert)
  },
  put (concert) {
    return Api().put(`concerts/${concert.id}`, concert)
  },
  delete (concert) {
    return Api().delete(`concerts/${concert}`)
  }
}
