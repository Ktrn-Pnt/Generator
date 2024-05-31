Тест генераторов случайных чисел с помощью тестов NIST

Результаты тестов хранятся в файле result.txt

Были протестированы генератор основанный на вихре Мерсена и генератор такого вида:
X[i+1] = 7*R*X[i] + R^2 - 11*R mod 127 

Где R = 17*N^2 + 5*N + 2

При небольшой выборке (100 чисел) генератор описанный выше проходит, примерно, половину тестов:

- FAILED - score: 0.001 - Monobit - слишком много нулей или единиц
- PASSED - score: 0.444 - Frequency Within Block - частота повторения в блоке длины m бит приблизительна равна m/2
- PASSED - score: 0.085 - Runs - последовательности нулей и единиц различной длины достаточно случайные 
- PASSED - score: 0.043 - Longest Run Ones In A Block - самая длинная серия единиц соответствует случайной последовательности 
- FAILED - score: 0.0 - Discrete Fourier Transform - есть повторяющиеся последовательности расположенные друг рядом с другом
- PASSED - score: 0.984 - Non Overlapping Template Matching - непериодические шаблоны встречаются не часто
- PASSED - score: 0.564 - Serial - не часто встречаются m битные последовательности единиц
- PASSED - score: 0.011 - Approximate Entropy - равномерно распределены m-битовые слова 
- FAILED - score: 0.002 - Cumulative Sums - слишком много нулей или единиц в начале последовательности
- FAILED - score: 0.172 - Random Excursion - отклонение от распределения числа появлений подпоследовательностей определённого вида
- FAILED - score: 0.196 - Random Excursion Variant - отклонение от распределения числа появлений подпоследовательностей определённого вида 

При увеличении выборки в 10 раз генератор проходит только один тест:

- PASSED - score: 0.062 - Non Overlapping Template Matching


У генератора, основанном на вихре Мерсена, дела обстоят лучше, при выборке в 100 чисел не проходит только один тест:

- FAILED - score: 0.096 - Random Excursion

При увеличении выборки в 10 раз не проходит уже 5 тестов:

- FAILED - score: 0.0 - Discrete Fourier Transform 
- FAILED - score: 0.0 - Serial 
- FAILED - score: 0.0 - Approximate Entropy 
- FAILED - score: 0.0 - Cumulative Sums 
- FAILED - score: 0.683 - Random Excursion 
