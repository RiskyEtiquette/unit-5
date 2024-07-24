document.querySelectorAll('.edit-movie-rating').forEach(button => {
    button.addEventListener('click', () => {
      const newScore = prompt('What is your new score for this movie?');
  
      if (newScore !== null) {
        const formInputs = {
          updated_score: newScore,
          rating_id: button.id,
        };
  
        fetch('/update_rating', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            document.querySelector(`span.rating_num_${button.id}`).textContent = newScore;
          } else {
            alert('Failed to update rating.');
          }
        });
      }
    });
  });
  