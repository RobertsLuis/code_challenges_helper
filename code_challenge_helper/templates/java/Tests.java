/**
 * Testes para a resolução do problema: {problem_name}
 *
 * Data: {date}
 */

 import org.junit.jupiter.api.Test;
 import static org.junit.jupiter.api.Assertions.assertEquals;
 
 /**
  * Para executar os testes, você precisará adicionar o JUnit 5 às dependências:
  * 
  * Se estiver usando Maven:
  * <dependencies>
  *     <dependency>
  *         <groupId>org.junit.jupiter</groupId>
  *         <artifactId>junit-jupiter</artifactId>
  *         <version>5.9.2</version>
  *         <scope>test</scope>
  *     </dependency>
  * </dependencies>
  * 
  * Se estiver usando Gradle:
  * testImplementation 'org.junit.jupiter:junit-jupiter:5.9.2'
  */

 public class Tests {
     @Test
     public void testBasic() {
         Solution solution = new Solution();
         assertEquals(5, solution.solution(2, 3));
         assertEquals(0, solution.solution(-1, 1));
         assertEquals(0, solution.solution(0, 0));
     }
 }