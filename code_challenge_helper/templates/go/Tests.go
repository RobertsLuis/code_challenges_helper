/**
 * Testes para a resolução do problema: {problem_name}
 *
 * Data: {date}
 */

package solution_test

import (
    "testing"

    "./solution" // Importe o pacote da solução
)

/**
 * Para executar os testes, você precisará usar o comando Go test:
 *
 * go test -v
 *
 * Certifique-se de que o Go está instalado e configurado corretamente no seu sistema.
 */

func TestBasic(t *testing.T) {
    testCases := []struct {
        a        int
        b        int
        expected int
    }{
        {2, 3, 5},
        {-1, 1, 0},
        {0, 0, 0},
    }

    for _, tc := range testCases {
        result := solution.Solution(tc.a, tc.b)
        if result != tc.expected {
            t.Errorf("Solution(%d, %d) = %d; esperado %d", tc.a, tc.b, result, tc.expected)
        }
    }
}