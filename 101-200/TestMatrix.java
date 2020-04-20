class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {

        int colNum = matrix.length;
        int rowNum = matrix[0].length;

        List<Integer> result = new ArrayList();

        int loops = (rowNum+1)/2;
        for(int loopNum=0; loopNum<loops; loopNum++){
            for(int j=loopNum; j<colNum-loopNum; j++){
                System.out.println("--"+matrix[loopNum][j]);
                result.add(matrix[loopNum][j]);
            }
            for(int j=loopNum+1; j<rowNum-loopNum; j++){
                                System.out.println("--"+matrix[j][colNum-loopNum-1]);

                result.add(matrix[j][colNum-loopNum-1]);
            }

            for(int j=rowNum-loopNum-2; j>=loopNum; j--){
                                System.out.println("--"+matrix[rowNum-loopNum-1][j]);

                result.add(matrix[rowNum-loopNum-1][j]);
            }

            for(int j=rowNum-loopNum-2; j>loopNum; j--){
                                System.out.println("--"+matrix[j][loopNum]);

                result.add(matrix[j][loopNum]);
            }
        }

        return result;

    }
}
