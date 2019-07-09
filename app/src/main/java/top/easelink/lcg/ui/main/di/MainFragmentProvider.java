package top.easelink.lcg.ui.main.di;

import dagger.Module;
import dagger.android.ContributesAndroidInjector;
import top.easelink.lcg.ui.main.article.view.ArticleFragment;
import top.easelink.lcg.ui.main.articles.view.ArticlesFragment;

@Module
public abstract class MainFragmentProvider {

    @ContributesAndroidInjector(modules = ArticlesFragmentModule.class)
    abstract ArticlesFragment provideArticlesFragmentFactory();

    @ContributesAndroidInjector()
    abstract ArticleFragment provideArticleFragmentFactory();

}