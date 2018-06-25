import gulp from 'gulp';
import merge from 'merge-stream';
import changedInPlace from 'gulp-changed-in-place';
import project from '../aurelia.json';

export default function deployAssets() {
  const taskImages = gulp.src( 'assets/images/*' )
    .pipe( changedInPlace( { firstPass: true } ) )
    .pipe( gulp.dest( `${project.platform.output}/images` ) );

  const taskScss = gulp.src( 'assets/scss/*' )
    .pipe( changedInPlace( { firstPass: true } ) )
    .pipe( gulp.dest( `${project.platform.output}/scss` ) );

  return taskImages;
}
