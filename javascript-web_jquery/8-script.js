$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    const allFilms = data.results;
    allFilms.forEach(film => {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});
